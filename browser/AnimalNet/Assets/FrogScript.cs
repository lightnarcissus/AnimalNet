using UnityEngine;
using System.Collections;

public class FrogScript : MonoBehaviour {

	public string packetType="tcp";
	private int ttl_main=7;
	public Vector3 currentTarget;
	private float hopTimer=0f;
	// Use this for initialization
	void Start () {
		StartCoroutine ("PrepareToLive");
		StartCoroutine ("StartHopping");
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
	public void AssignDestination()
	{
		hopTimer = 0f;
		Debug.Log ("assigning new destination");
		currentTarget=PondManager.Instance.pondList[Random.Range(0,PondManager.Instance.pondList.Count-1)].transform.position;
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
			if (time % 1f < 0.1f) {
				AssignDestination ();
			}
			yield return 0;
		}
		DisappearDestroy ();
		yield return null;
	}

	IEnumerator StartHopping()
{
		while(hopTimer<1f)
		{
			hopTimer += Time.deltaTime;
			transform.position = Vector3.Lerp (transform.position, currentTarget, hopTimer);
			yield return 0;
		}
		yield return null;
	}

	void DisappearDestroy()
	{
		
		Destroy (gameObject);
	}
}
