using UnityEngine;
using System.Collections;

public class FrogScript : MonoBehaviour {

	public string packetType="tcp";

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	public void AssignIP(string ipAddr)
	{
		
	}

	public void AssignChannel(int channel)
	{
		if (channel == 5) {
			Debug.Log ("assigned 5 channel");
			GetComponent<Animator> ().speed = 5;
		}
	}

	public void ChangeType(string packetType)
	{
		switch (packetType) {
		case "ip":
			GetComponent<SpriteRenderer> ().color = Color.red;
			gameObject.name = "frog_ip";
			break;
		case "tcp":
			break;
		case "http":
			GetComponent<SpriteRenderer> ().color = Color.yellow;
			gameObject.name = "frog_http";
			break;
		case "wlan":
			GetComponent<SpriteRenderer> ().color = Color.blue;
			gameObject.name = "frog_wlan";
			break;
		case "ssl":
			gameObject.name = "frog_ssl";
			break;
		}
	}
}
