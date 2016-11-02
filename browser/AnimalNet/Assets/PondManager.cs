using UnityEngine;
using System.Collections;
using System.Collections.Generic;
public class PondManager : MonoBehaviour {

	public List<string> activeAddress;
	public GameObject pondPrefab;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	public void CheckAdd(string address)
	{
		Vector3 newpos=Camera.main.ScreenToWorldPoint(new Vector3(UnityEngine.Random.Range (0f, Screen.width), UnityEngine.Random.Range (0f, Screen.height),2f));
		if (activeAddress.Count == 0) {
			GameObject tempObj = Instantiate (pondPrefab, newpos, Quaternion.identity) as GameObject;
			tempObj.transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = address;
			activeAddress.Add (address);
		}
		if(!activeAddress.Contains(address))
		{
				GameObject tempObj = Instantiate (pondPrefab, newpos, Quaternion.identity) as GameObject;
				tempObj.transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = address;
				activeAddress.Add (address);
		}
	}
}
