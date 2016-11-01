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

	public void ChangeType(string packetType)
	{
		switch (packetType) {
		case "ip":
			GetComponent<SpriteRenderer> ().color = Color.red;
			break;
		case "tcp":
			break;
		case "http":
			GetComponent<SpriteRenderer> ().color = Color.yellow;
			break;
		case "udp":
			GetComponent<SpriteRenderer> ().color = Color.blue;
			break;
		case "ssl":
			break;
		}
	}
}
