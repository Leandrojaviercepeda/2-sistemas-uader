package ar.com.gugler.cursos.clase1;

import java.util.Scanner;

public class Ejercicio2 {

	private static Scanner t;

	public static void main(String[] args) {
		t = new Scanner(System.in);
		System.out.println("Ingrese su Nombre");
		String texto = t.nextLine();
		System.out.println("Hola " + texto);
	}	

}