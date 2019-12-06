package ej2;

/**
 * @author Leandro Javier Cepeda
 *
 */
public class Punto {

	private double x, y;

	/**
	 * Constructor.
	 * 
	 * @param Double x: coordenada eje x.
	 * @param Double y: coordenada eje y.
	 */
	public Punto(double x, double y) {
		this.x = x;
		this.y = y;
	}

	public double getX() {
		return x;
	}

	public void setX(double x) {
		this.x = x;
	}

	public double getY() {
		return y;
	}

	public void setY(double y) {
		this.y = y;
	}

	/**
	 * Muestra el punto.
	 * 
	 * @return String datos: coordenada eje x, coordenada eje y.
	 */
	public String imprimir() {
		String salida = String.format("\nCoordenada eje x: %f \nCoordenada eje y: %f", this.x, this.y);
		return salida;
	}

}
