package vektorelCarpim;

import java.util.Vector;
	
public class vektorClass {
	
  	static Vector<Integer> vector1 = new Vector<>();
  	static Vector<Integer> vector2 = new Vector<>();
  	
  	private static int carpim(Vector<Integer> v1, Vector<Integer> v2){
  		int toplam=0;
  		
  		if(v1.size() != v2.size()) return 0;
  		
  		for(int i = 0; i<v1.size(); i++){
  			toplam = toplam + (v1.get(i)*v2.get(i));
  		}
  		
  		return toplam;
  	}
  	
     public static void main(String[] args) {
  	  vector1.add(1);
  	  vector1.add(2);
  	  vector1.add(3);
  	  vector1.add(5);
  	  
  	  vector2.add(2);
  	  vector2.add(4);
  	  vector2.add(6);
  	  vector2.add(7);
  	  
  	  System.out.println(String.valueOf(carpim(vector1, vector2)));
  	  
  	  
  }
}