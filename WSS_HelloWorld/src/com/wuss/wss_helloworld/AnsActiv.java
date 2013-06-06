package com.wuss.wss_helloworld;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.widget.EditText;


public class AnsActiv extends Activity {
	
	private EditText mtv;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.ans_layout);
		
		mtv = (EditText) findViewById(R.id.editText1);
		Bundle bundle = this.getIntent().getBundleExtra("bundle");
		String[] result = bundle.getStringArray("result");
		
		for(String s : result) {
			mtv.setText(mtv.getText().toString() + "\n"+s);
		}
	}
	


	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
}
