package ej3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ejercicio3 {
	/*
	 * Implemente un programa que indique si una palabra es un palíndromo. Una
	 * palabra es palidromo si se lee igual de izquierda a derecha que de
	 * derecha a izquierda.
	 */
	public static void main(String[] args) throws IOException {
		BufferedReader t = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Ingrese una palabra");
		String palabra = t.readLine();
		System.out.println(palabraInversa(palabra));
	}

	public static String palabraInversa(String palabra) {
		String palabra_inversa = "";

		for (int i = palabra.length() - 1; i >= 0; i--) {
			palabra_inversa += palabra.charAt(i);
		}

		if (palabra_inversa.equals(palabra)) {
			return "Es Palindromo";
		} else {
			return "No es Palindromo";
		}
	}

}
