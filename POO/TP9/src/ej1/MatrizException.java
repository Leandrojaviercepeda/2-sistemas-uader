package ej1;

public class MatrizException extends Exception {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	static String Errores[] = {"E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14", "E15"};

	String name;

	MatrizException(String nom) {
		name = nom;
	}

	MatrizException(int numError) {
		name = Errores[numError];
	}

	public String getName() {
		return this.name;
	}
	
	public String toString() {
		return "ERROR MATRIZ : " + name;
	}
}
