package com.wuss.wss_helloworld;

import java.util.ArrayList;
import java.util.List;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends Activity {

	private static final String TAG = "com.wuss.wss_helloworld";
	private EditText et_ans;
	private EditText et_num1;
	private EditText et_num2;
	private EditText et_num3;
	private EditText et_num4;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		init();
	}

	private void init() {
		et_ans = (EditText) findViewById(R.id.editText_ans);
		et_num1 = (EditText) findViewById(R.id.editText_num1);
		et_num2 = (EditText) findViewById(R.id.editText_num2);
		et_num3 = (EditText) findViewById(R.id.editText_num3);
		et_num4 = (EditText) findViewById(R.id.editText_num4);
	}
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
	public void myExit(View v){
		Log.v(TAG,"myExit");
		this.finish();
	}
	
	public void onResetClicked(View v){
		Log.v(TAG,"Reset");
		this.et_num1.setText("1");
		this.et_num2.setText("2");
		this.et_num3.setText("3");
		this.et_num4.setText("4");
		this.et_ans.setText("24");
	}

	public void onCalcButtonClicked(View v){
		Log.v(TAG, "calc");
		int ans = Integer.parseInt(et_ans.getText().toString());
		int num1 = Integer.parseInt(et_num1.getText().toString());
		int num2 = Integer.parseInt(et_num2.getText().toString());
		int num3 = Integer.parseInt(et_num3.getText().toString());
		int num4 = Integer.parseInt(et_num4.getText().toString());
		ArrayList<Integer> l = new ArrayList<Integer>();
		l.add(ans);
		l.add(num1);
		l.add(num2);
		l.add(num3);
		l.add(num4);
		String[] result = new Calculate_TwentyFour().calculate24(l);
		Intent intent_ans = new Intent(this, AnsActiv.class);
		Bundle bundle = new Bundle();
		bundle.putStringArray("result", result);
		intent_ans.putExtra("bundle", bundle);
		startActivity(intent_ans);
		
	}
	
    class Calculate_TwentyFour{
    	private ArrayList<String> Result_Data;
    	private Double Ans;
		public String[] calculate24(List<Integer> l){
			Ans = (double)l.get(0);
			ArrayList<Integer> argus = new ArrayList<Integer>();
			argus.add(l.get(1));
			argus.add(l.get(2));
			argus.add(l.get(3));
			argus.add(l.get(4));
			
			//reorder argus
			//generate all orders of the argus and save to argus_list
			ArrayList<ArrayList<Integer>> argus_list = new ArrayList<ArrayList<Integer>>(); 
			for (int i=0; i<24; i++){
				int a1 = (i%12)/3;
				int a2 = i%3;
				int a3 = i/12;
				ArrayList<Integer> t_alist = new ArrayList<Integer>();
				@SuppressWarnings("unchecked")
				ArrayList<Integer> t_argus = (ArrayList<Integer>) argus.clone();
				t_alist.add(t_argus.remove(a1));
				t_alist.add(t_argus.remove(a2));
				t_alist.add(t_argus.remove(a3));
				t_alist.add(t_argus.remove(0));
				if (!argus_list.contains(t_alist)) argus_list.add(t_alist);
			}
			
			Result_Data = new ArrayList<String>();
			for (ArrayList<Integer> t_alist:argus_list){
				calculate24_each(t_alist);
			}
			
			Result_Data.add(0,"Totally "+String.valueOf(Result_Data.size())+" expressions!");
			String[] result = new String[Result_Data.size()]; 
			Result_Data.toArray(result);
			return result;
		}
		
		private void calculate24_each(ArrayList<Integer> tl){
			
			ArrayList<Double> num_list = new ArrayList<Double>();
			ArrayList<String> expr_list = new ArrayList<String>();
			for (Integer bi : tl){
				num_list.add((double) bi);
				expr_list.add(String.valueOf(bi));
			}
			for (Integer i=0;i<64;i++){
				calculateManager(determineOP(i),num_list,expr_list);
			}
			return;

		}
		private ArrayList<Integer> determineOP (Integer i){
			ArrayList<Integer> result = new ArrayList<Integer>();
			result.add(i/16);
			result.add((i%16)/4);
			result.add(i%4);
			return result;
		}
		
		@SuppressWarnings("unchecked")
		private void calculateManager(ArrayList<Integer> op, ArrayList<Double> num_list, ArrayList<String> expr_list){
			if (num_list.size() == 1) {
				if (num_list.get(0).equals(Ans)){
					Result_Data.add(expr_list.get(0));
				}
				return;
			}
			for (Integer i=0;i<num_list.size()-1;i++){
				ArrayList<Integer> new_op = (ArrayList<Integer>) op.clone();
				ArrayList<Double> new_num_list = (ArrayList<Double>) num_list.clone();
				ArrayList<String> new_expr_list = (ArrayList<String>) expr_list.clone();
				String expr_a = new_expr_list.remove((int) i);
				String expr_b = new_expr_list.remove((int) i);
				Double num_a = new_num_list.remove((int) i);
				Double num_b = new_num_list.remove((int) i);
				Integer o = new_op.remove((int) i);
				Struct_String_Double t_ssd = getResultByOp(o,num_a,num_b);
				new_num_list.add(i, t_ssd.num);
				new_expr_list.add(i, "("+expr_a+t_ssd.expr+expr_b+")");
				calculateManager(new_op, new_num_list, new_expr_list);
			}
		}
		
		private Struct_String_Double getResultByOp(Integer o, Double a, Double b){
			if (o==0){
				return new Struct_String_Double("+",a+b);
			}
			if (o==1){
				return new Struct_String_Double("-",a-b);
			}
			if (o==2){
				return new Struct_String_Double("*",a*b);
			}
			if (o==3){
				if (b==0) return new Struct_String_Double("/",99999999999.0);
				return new Struct_String_Double("/",a/b);
			}
			return null;
		}
		
		class Struct_String_Double{
			Struct_String_Double(String e, Double n){
				expr = e;
				num = n;
			}
			String expr;
			Double num;
		}
	}
}
