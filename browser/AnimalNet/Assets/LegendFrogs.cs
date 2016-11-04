using UnityEngine;
using System.Collections;

public class LegendFrogs : MonoBehaviour {

	public float speed=2f;
	// Use this for initialization
	void Start () {
		GetComponent<Animator> ().speed = speed;
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
