using UnityEngine;
using System.Collections;
using System.Collections.Generic;
public class PondManager : MonoBehaviour {

	public List<string> activeAddress;
	public List<GameObject> pondList;
	public GameObject pondPrefab;
	public float maxSignal = -80f;
	public int minSignal = -20;
	//SINGLETON
	private static PondManager _instance;

	public static PondManager Instance
	{
		get
		{
			return _instance;
		}
	}

	void Awake()
	{

		if (_instance != null)
		{
			Debug.Log("Instance already exists!");
			return;
		}
		_instance = this;
	}

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
			pondList.Add (tempObj);
		}
		if(!activeAddress.Contains(address))
		{

			GameObject tempObj = Instantiate (pondPrefab, newpos, Quaternion.identity) as GameObject;
				tempObj.transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = address;
				activeAddress.Add (address);
			pondList.Add (tempObj);
		}
	}


	public void ConveySignalStrength(int strength)
	{
		Debug.Log ("STRENGTH: " + strength);
		float opacity = strength / maxSignal;
		Debug.Log (opacity);
		if (pondList.Count > 0) {
			Color currentColor = pondList [pondList.Count - 1].GetComponent<SpriteRenderer> ().color;
			pondList [pondList.Count - 1].GetComponent<SpriteRenderer> ().color = new Color (currentColor.r, currentColor.g,currentColor.b, opacity);
		}
	}

	public void AssignUserAgent(string userAgent)
	{
		if (pondList.Count > 0) {
			pondList [pondList.Count - 1].transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = userAgent;
		}
	}
	public void AssignSSID(string userAgent)
	{
		if (pondList.Count > 0) {
			pondList [pondList.Count - 1].transform.GetChild (0).gameObject.GetComponent<TextMesh> ().text = userAgent;
		}
	}

}
