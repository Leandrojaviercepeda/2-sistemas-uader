package ej1;

import ej1.Matriz;

public class CalculadoraDeMatriz {

	public Matriz sumaMatriz(Matriz matriz1, Matriz matriz2) {
		Integer[][] m1 = matriz1.getMatriz();
		Integer[][] m2 = matriz2.getMatriz();
		
		if (mismaDimension(matriz1, matriz2)) {
			for (int f = 0; f < matriz1.getTamanioFilas(); f++) {
				for (int c = 0; c < matriz1.getTamanioColumnas(); c++) {
					m1[f][c] += m2[f][c];
				}
			}
			return new Matriz(m1);
		} else {
			System.out.println("No es posible realizar la suma");
			return new Matriz(new Integer[0][0]);
		}
	}
	
	
	public Matriz restaMatriz(Matriz matriz1, Matriz matriz2) {
		Integer[][] m1 = matriz1.getMatriz();
		Integer[][] m2 = matriz2.getMatriz();

		if (mismaDimension(matriz1, matriz2)) {
			for (int f = 0; f < matriz1.getTamanioFilas(); f++) {
				for (int c = 0; c < matriz1.getTamanioColumnas(); c++) {
					m1[f][c] -= m2[f][c];
				}
			}
			return new Matriz(m1);
		} else {
			System.out.println("No es posible realizar la resta");
			return new Matriz(new Integer[0][0]);
		}
	}

	public Matriz productoMatriz(Matriz matriz1, Matriz matriz2) {

		if (condicionProducto(matriz1, matriz2)) {
			int suma;
			Integer[][] m3 = new Integer[matriz1.getTamanioFilas()][matriz2
			                                                        .getTamanioColumnas()];

			for (int x = 0; x < matriz1.getTamanioFilas(); x++) {
				for (int y = 0; y < matriz2.getTamanioColumnas(); y++) {
					suma = 0;
					for (int z = 0; z < matriz1.getTamanioColumnas(); z++)
						suma += matriz1.getMatriz()[x][z]
								* matriz2.getMatriz()[z][y];

					m3[x][y] = suma;
				}
			}
			return new Matriz(m3);
		} else {
			System.out
			.println("El nro. de filas de la 1° matriz es <> del nro. de columnas de la 2°.");
			return new Matriz(new Integer[0][0]);
		}
	}

	public void rellenarMatriz(Matriz matriz1) {
		Integer[][] matrizAux = new Integer[matriz1.getTamanioFilas()][matriz1
				.getTamanioColumnas()];

		for (int f = 0; f < matriz1.getTamanioFilas(); f++) {
			for (int c = 0; c < matriz1.getTamanioColumnas(); c++) {
				matrizAux[f][c] = (int) (Math.random() * 10) + 1;
			}
		}
		matriz1.setMatriz(matrizAux);
	}

	public boolean condicionProducto(Matriz matriz1, Matriz matriz2) {
		if (matriz1.getTamanioColumnas() == matriz2.getTamanioFilas()) {
			return true;
		} else {
			return false;
		}
	}

	public boolean mismaDimension(Matriz matriz1, Matriz matriz2) {

		if (matriz1.getTamanioColumnas() == matriz2.getTamanioColumnas()
				& matriz1.getTamanioFilas() == matriz2.getTamanioFilas()) {
			return true;
		} else {
			return false;
		}
	}
	

	public void mostrarMatriz(Matriz matriz1) {
		Integer[][] matrizAux = matriz1.getMatriz();
		for (int f = 0; f < matriz1.getTamanioFilas(); f++) {
			for (int c = 0; c < matriz1.getTamanioColumnas(); c++) {
				System.out.print(matrizAux[f][c] + " ");
			}
			System.out.println();
		}
	}
	
	public void mostrarMatriz2(Integer[][] matriz1) {
		for (int f = 0; f < matriz1.length; f++) {
			for (int c = 0; c < matriz1[0].length; c++) {
				System.out.print(matriz1[f][c] + " ");
			}
			System.out.println();
		}
	}
}
