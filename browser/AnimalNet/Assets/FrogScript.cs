using UnityEngine;
using System.Collections;

public class FrogScript : MonoBehaviour {

	public string packetType="tcp";
	private int ttl_main=7;
	// Use this for initialization
	void Start () {
		StartCoroutine ("PrepareToLive");
	
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
			GetComponent<Animator> ().SetBool ("Green", true);
			//GetComponent<SpriteRenderer> ().color = Color.red;
			gameObject.name = "frog_ip";
			break;
		case "http":
			GetComponent<Animator> ().SetBool ("Blue", true);
			gameObject.name = "frog_http";
			break;
		case "wlan":
			GetComponent<Animator> ().SetBool ("Yellow", true);
			gameObject.name = "frog_wlan";
			break;
		case "ssl":
			GetComponent<Animator> ().SetBool ("Pink", true);
			gameObject.name = "frog_ssl";
			break;
		}
	}
	public void AssignDestination(string dest)
	{
		
	}
	public void SetTTL(int ttl)
	{
		ttl_main = ttl;
	}
	public void GiveCookie(string packetType)
	{
		
	}


	IEnumerator PrepareToLive()
	{
		float time = 0f;
		while (time < ttl_main) {
			time += Time.deltaTime;
			yield return 0;
		}
		DisappearDestroy ();
		yield return null;
	}

	void DisappearDestroy()
	{
		
		Destroy (gameObject);
	}
}
