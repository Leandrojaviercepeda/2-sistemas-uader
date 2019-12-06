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

public class PruebaIteraciones {
	
	public static void main(String[] args){
		
		System.out.println();
		Iteracion arraynumeros = new Iteracion();
		arraynumeros.arrayNumeros();

		System.out.println("Devuelve los valores del Arrayist usando un For.");
		System.out.println(arraynumeros.arrayNumerosFor());
		System.out.println();

		System.out.println("Devuelve los valores del Arrayist usando un While.");
		System.out.println(arraynumeros.arrayNumerosWhile());
		System.out.println();

		System.out.println("Devuelve los valores del Arrayist usando un iterador.");
		System.out.println(arraynumeros.arrayNumerosIterador());
		System.out.println();

		System.out.println("Devuelve los valores del Arrayist usando un iterador.");
		System.out.println(arraynumeros.arrayNumerosMayoresADiez());
		System.out.println();
		
		
		Iteracion hashsetnumeros = new Iteracion();
		hashsetnumeros.hashsetNumeros();
		
		System.out.println("Devuelve los valores del HashSet usando un For.");
		System.out.println(hashsetnumeros.hashsetNumerosFor());
		System.out.println();
		
		System.out.println("Devuelve los valores del HashSet usando un While.");
		System.out.println(hashsetnumeros.hashsetNumerosWhile());
		System.out.println();
		
		System.out.println("Devuelve los valores del HashSet usando un iterador.");
		System.out.println(hashsetnumeros.hashsetNumerosIterador());
		System.out.println();
		
		
		System.out.println("Devuelve los valores mayores a diez del HashSet usando un iterador.");
		System.out.println(hashsetnumeros.hashsetNumerosMayoresADiez());
		System.out.println();
		
		
		
		

		
	}
}
