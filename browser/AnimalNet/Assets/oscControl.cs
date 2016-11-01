//
//	  UnityOSC - Example of usage for OSC receiver
//
//	  Copyright (c) 2012 Jorge Garcia Martin
//
// 	  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
// 	  documentation files (the "Software"), to deal in the Software without restriction, including without limitation
// 	  the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
// 	  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// 
// 	  The above copyright notice and this permission notice shall be included in all copies or substantial portions 
// 	  of the Software.
//
// 	  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
// 	  TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
// 	  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
// 	  CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
// 	  IN THE SOFTWARE.
//

using UnityEngine;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using UnityOSC;

public class oscControl : MonoBehaviour {
	
	private Dictionary<string, ServerLog> servers;
	private Dictionary<string, ClientLog> clients;
	private float randVal=0f;
	public GameObject frogSprite;
	private String msg="";
	// Script initialization
	void Start() {	
		OSCHandler.Instance.Init(); //init OSC
		servers = new Dictionary<string, ServerLog>();
		clients = new Dictionary<string,ClientLog> ();
	}

	// NOTE: The received messages at each server are updated here
    // Hence, this update depends on your application architecture
    // How many frames per second or Update() calls per frame?
	void Update() {
		
		OSCHandler.Instance.UpdateLogs();

		msg="0.1544944";
		byte[] val = new byte[]{176,8,0};

		servers = OSCHandler.Instance.Servers;
		clients = OSCHandler.Instance.Clients;
		if (UnityEngine.Random.value < 0.01f) {
			randVal = UnityEngine.Random.Range (0f, 0.7f);
			Debug.Log ("sending messages");
		//	OSCHandler.Instance.SendMessageToClient ("localhost", "/user/1", randVal);
		//	OSCHandler.Instance.SendMessageToClient ("localhost", "/user/2", randVal);
		//	OSCHandler.Instance.SendMessageToClient ("localhost", "/user/3", randVal);
		//	OSCHandler.Instance.SendMessageToClient ("localhost", "/user/4", randVal);
		}
		OSCHandler.Instance.UpdateLogs();

		foreach (KeyValuePair<string, ServerLog> item in servers) {
			// If we have received at least one packet,
			// show the last received from the log in the Debug console
			if (item.Value.log.Count > 0) {
				int lastPacketIndex = item.Value.packets.Count - 1;
				UnityEngine.Debug.Log ("received something");
				UnityEngine.Debug.Log (String.Format ("SERVER: {0} ADDRESS: {1} VALUE : {2}", 
					                                    item.Key, // Server name
					                                    item.Value.packets [lastPacketIndex].Address, // OSC address
					                                    item.Value.packets [lastPacketIndex].Data [0].ToString ())); //First data value
				Vector3 newpos=Camera.main.ScreenToWorldPoint(new Vector3(UnityEngine.Random.Range (0f, Screen.width), UnityEngine.Random.Range (0f, Screen.height),2f));
				if (item.Value.packets [lastPacketIndex].Address == "Frog/init") {
					GameObject tempFrog = Instantiate (frogSprite, newpos, Quaternion.identity) as GameObject;
					tempFrog.GetComponent<FrogScript> ().AssignIP (item.Value.packets [lastPacketIndex].Data [0].ToString ());
				} else if (item.Value.packets [lastPacketIndex].Address == "Frog/ip") {
					GameObject tempFrog = Instantiate (frogSprite, newpos, Quaternion.identity) as GameObject;
					tempFrog.GetComponent<FrogScript> ().ChangeType ("ip");
				}
				else if (item.Value.packets [lastPacketIndex].Address == "Frog/tcp") {
					GameObject tempFrog = Instantiate (frogSprite, newpos, Quaternion.identity) as GameObject;
					tempFrog.GetComponent<FrogScript> ().ChangeType ("tcp");
				}
				else if (item.Value.packets [lastPacketIndex].Address == "Frog/http") {
					GameObject tempFrog = Instantiate (frogSprite, newpos, Quaternion.identity) as GameObject;
					tempFrog.GetComponent<FrogScript> ().ChangeType ("http");
				}
				else if (item.Value.packets [lastPacketIndex].Address == "Frog/udp") {
					GameObject tempFrog = Instantiate (frogSprite, newpos, Quaternion.identity) as GameObject;
					tempFrog.GetComponent<FrogScript> ().ChangeType ("udp");
				}else if (item.Value.packets [lastPacketIndex].Address == "Frog/ssl") {
					GameObject tempFrog = Instantiate (frogSprite, newpos, Quaternion.identity) as GameObject;
					tempFrog.GetComponent<FrogScript> ().ChangeType ("ssl");
				}
			}
		}
			

		foreach( KeyValuePair<string, ClientLog> item in clients )
		{
			// If we have sent at least one message,
			// show the last sent message from the log in the Debug console
			if(item.Value.log.Count > 0) 
			{
				int lastMessageIndex = item.Value.messages.Count- 1;
				
				UnityEngine.Debug.Log(String.Format("CLIENT: {0} ADDRESS: {1} VALUE 0: {2}", 
				                                    item.Key, // Server name
				                                    item.Value.messages[lastMessageIndex].Address, // OSC address
				                                    item.Value.messages[lastMessageIndex].Data[0].ToString())); //First data value
				                                    
			}

		}
	}
}