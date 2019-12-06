package ej1;

public class Matriz {

	private Integer[][] matriz;

	public Matriz(Integer[][] matriz) {
		this.matriz = matriz;
	}

	public Integer[][] getMatriz() {
		return matriz;
	}

	public void setMatriz(Integer[][] matriz) {
		this.matriz = matriz;
	}		
	
	public int getTamanioColumnas() {
		return this.matriz[0].length;
	}

	public int getTamanioFilas() {
		return this.matriz.length;
	}
	
	

}
