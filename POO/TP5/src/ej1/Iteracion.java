/**
 * Nombre de la clase: Iteracion
 * 
 * Informacion de la Version:
 * En una clase que contenga un método “main” declare un ArrayList con 20 Numeros aleatorios 
 * a. Imprima los elementos cargados en la colección usando un ciclo for. 
 * b. Imprima los elementos cargados en la colección usando un iterador. 
 * c. Imprima los elementos cargados en la colección usando un ciclo while. 
 * d. Itere la lista imprimiendo sólo los números mayores a 10.
 * e. Realizar lo mismo con un HashSet.
 * 
 * Fecha: 
 *  
 */

package ej1;

import java.util.ArrayList;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Random;

public class Iteracion {
	
	private Random r = new Random();
	private ArrayList<Integer> arrayNumeros;
	private HashSet<Integer> hashsetNumeros;
	int rangoValores = 100;
	
	public Iteracion() {
		super();
		this.arrayNumeros = new ArrayList<Integer>();
		this.hashsetNumeros = new HashSet<Integer>();
	}
	
	public HashSet<Integer> getHashsetNumeros() {
		return hashsetNumeros;
	}

	public void setHashsetNumeros(HashSet<Integer> hashsetNumeros) {
		this.hashsetNumeros = hashsetNumeros;
	}

	public ArrayList<Integer> getArrayNumeros() {
		return arrayNumeros;
	}

	public void setArrayNumeros(ArrayList<Integer> arrayNumeros) {
		this.arrayNumeros = arrayNumeros;
	}
	
	//Completa el ArrayList con 20 numeros aleatorios de 1 a 100.
	public void arrayNumeros(){
		for (int i = 0; i <= 20; i++){
			this.arrayNumeros.add(r.nextInt(rangoValores));
		}
	}
	
	//Devuelve los valores del ArrayList usando ciclo For.
	public String arrayNumerosFor(){
		String stringsalida = "";
		for (int numero: this.arrayNumeros) {
			stringsalida += Integer.toString(numero) + ", ";
		}	
		return stringsalida;
	}

	//Devuelve los valores del ArrayList usando ciclo While.
	public String arrayNumerosWhile(){
		String stringsalida = "";
		int i = 0;
		while (i < this.arrayNumeros.size()){
			int numero = this.arrayNumeros.get(i);
			stringsalida += Integer.toString(numero) + ", ";
			i += 1;
		}
		return stringsalida;
	}
	
	//Devuelve los valores del ArrayList usando un iterador.
	public String arrayNumerosIterador(){
		String stringsalida = "";
		Iterator <Integer> iterador = arrayNumeros.iterator();
		while(iterador.hasNext()){
			int numero = iterador.next();
			stringsalida += Integer.toString(numero) + ", ";
		}
		return stringsalida;
	}
	
	//Devuelve los valores mayores a diez del ArrayList usando un iterador.	
	public String arrayNumerosMayoresADiez(){
		String stringsalida = "";
		Iterator <Integer> iterador = arrayNumeros.iterator();
		while(iterador.hasNext()){
			int numero = iterador.next();
			if (numero > 10){
				stringsalida += Integer.toString(numero)+ ", ";
			}
		}
		return stringsalida;
	}
	
	//Completa el HashSet con 20 numeros aleatorios de 1 a 100.
	public void hashsetNumeros(){
		for (int i = 0; i <= 20; i++){
			this.hashsetNumeros.add(r.nextInt(rangoValores));
		}
	}
	
	//Devuelve los valores del HashSet usando ciclo For.
	public String hashsetNumerosFor(){
		String stringsalida = "";
		for (int numero: this.hashsetNumeros) {
			stringsalida += Integer.toString(numero)+ ", ";
		}
		return stringsalida;
	}

	//Devuelve los valores del HashSet usando ciclo While.
	public String hashsetNumerosWhile(){
		String stringsalida = ""; 
		int i = 0;
		while (i <= rangoValores){
			if (this.hashsetNumeros.contains(i)){
				stringsalida += Integer.toString(i) + ", ";
			}
			i += 1;
		}
		return stringsalida;
	}
	
	//Devuelve los valores del HashSet usando un iterador.
	public String hashsetNumerosIterador(){
		String stringsalida = "";
		Iterator <Integer> iterador = hashsetNumeros.iterator();	
		while(iterador.hasNext()){
			int numero = iterador.next();
			stringsalida += Integer.toString(numero) + ", ";
		}
		return stringsalida;
	}
	
	//Devuelve los valores mayores a diez del HashSet usando un iterador.	
	public String hashsetNumerosMayoresADiez(){
		String stringsalida = "";
		Iterator <Integer> iterador = hashsetNumeros.iterator();
		while(iterador.hasNext()){
			int numero = iterador.next();
			if (numero > 10){
				stringsalida += Integer.toString(numero) + ", ";
			}
		}	
		return stringsalida;
	}
	
	
}
