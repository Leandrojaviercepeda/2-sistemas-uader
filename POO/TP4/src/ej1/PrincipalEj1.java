package ej1;

import java.io.IOException;

public class PrincipalEj1 {

	public static void main(String[] args) throws NumberFormatException, IOException {

		CalculadoraDeMatriz cdm = new CalculadoraDeMatriz();
		
		Matriz matriz1 = new Matriz(new Integer[2][3]);
		Matriz matriz2 = new Matriz(new Integer[3][3]);
		
		
		/*
		System.out.println("-------------------- Suma --------------------");

		cdm.rellenarMatriz(matriz1);
		cdm.rellenarMatriz(matriz2);

		System.out.println("Matriz A");
		cdm.mostrarMatriz(matriz1);

		System.out.println();

		System.out.println("Matriz B");
		cdm.mostrarMatriz(matriz2);

		System.out.println();

		System.out.println("MatrizA + MatrizB ");
		cdm.mostrarMatriz(cdm.sumaMatriz(matriz1, matriz2));

		System.out.println();
	
		
		System.out.println("-------------------- Diferencia --------------------");
		cdm.rellenarMatriz(matriz1);
		cdm.rellenarMatriz(matriz2);

		System.out.println("Matriz A");
		cdm.mostrarMatriz(matriz1);

		System.out.println();

		System.out.println("Matriz B");
		cdm.mostrarMatriz(matriz2);

		System.out.println();

		System.out.println("MatrizA - MatrizB ");
		cdm.mostrarMatriz(cdm.restaMatriz(matriz1, matriz2));

		System.out.println();

		*/
		System.out.println("-------------------- Producto --------------------");
		cdm.rellenarMatriz(matriz1);
		cdm.rellenarMatriz(matriz2);
		

		
		
		System.out.println("Matriz A");
		cdm.mostrarMatriz(matriz1);

		System.out.println();

		System.out.println("Matriz B");
		cdm.mostrarMatriz(matriz2);

		System.out.println();
		
		
		System.out.println("MatrizA * MatrizB ");
		cdm.mostrarMatriz(cdm.productoMatriz(matriz1, matriz2));
		
	}

}