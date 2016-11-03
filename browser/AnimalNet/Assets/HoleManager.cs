using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class HoleManager : MonoBehaviour {
	public List<string> activeAddress;
	public List<GameObject> holeList;
	public GameObject holePrefab;
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
			GameObject tempObj = Instantiate (holePrefab, newpos, Quaternion.identity) as GameObject;
			tempObj.transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = address;
			activeAddress.Add (address);
			holeList.Add (tempObj);
		}
		if(!activeAddress.Contains(address))
		{
			Quaternion randEuler = Quaternion.Euler (new Vector3 (0f, 0f, Random.Range (0f, 180f)));
			GameObject tempObj = Instantiate (holePrefab, newpos, randEuler) as GameObject;
			tempObj.transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = address;
			activeAddress.Add (address);
			holeList.Add (tempObj);
		}
	}

	public void AssignServer(string serverType)
	{
		Vector3 newpos=Camera.main.ScreenToWorldPoint(new Vector3(UnityEngine.Random.Range (0f, Screen.width), UnityEngine.Random.Range (0f, Screen.height),2f));

			GameObject tempObj = Instantiate (holePrefab, newpos, Quaternion.identity) as GameObject;
			tempObj.transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = serverType;

	}
}
