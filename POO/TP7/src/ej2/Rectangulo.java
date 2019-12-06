/**
 * 
 */
package ej2;

/**
 * @author Leandro Javier Cepeda
 *
 */
public class Rectangulo extends Forma {

	private double ladoMayor, ladoMenor;

	/**
	 * Constructor.
	 * 
	 * @param Punto  centro: coordenada x, coordenada y.
	 * @param String color: color de la forma.
	 * @param String nombre: nombre de la forma.
	 * @param Double ladoMayor: lado mayor del rectangulo.
	 * @param Double ladoMayor: lado menor del rectangulo.
	 */
	public Rectangulo(Punto centro, String color, String nombre, double ladoMayor, double ladoMenor) {
		super(centro, color, nombre);
		this.ladoMayor = ladoMayor;
		this.ladoMenor = ladoMenor;
	}

	public double getLadoMayor() {
		return ladoMayor;
	}

	public void setLadoMayor(double ladoMayor) {
		this.ladoMayor = ladoMayor;
	}

	public double getLadoMenor() {
		return ladoMenor;
	}

	public void setLadoMenor(double ladoMenor) {
		this.ladoMenor = ladoMenor;
	}

	/**
	 * Calcula el area del rectangulo.
	 * 
	 * @return Double area.
	 */
	public double area() {
		return this.ladoMayor * this.ladoMenor;
	}

	/**
	 * Calcula el perimetro del rectangulo.
	 * 
	 * @return Double perimetro.
	 */
	public double perimetro() {
		return 2 * this.ladoMayor + 2 * this.ladoMenor;
	}

	/**
	 * Cambia el tamaño del rectangulo. Así, por ejemplo, si el factor vale 2, el
	 * rectángulo duplicará su tamaño y si es 0,5 se reducirá a la mitad.
	 * 
	 * @params Double factor: factor de escala.
	 */
	public void cambiarTamaño(double factor) {
		this.ladoMayor = ladoMayor * factor;
		this.ladoMenor = ladoMenor * factor;
	}

	/**
	 * Muestra el rectagulo.
	 * 
	 * @return String datos: forma, color, centro eje x, centro eje y, lado mayor,
	 *         lado menor.
	 */
	public String imprimir() {
		String salida = String.format("\nLado mayor: %f \nLado menor: %f", this.ladoMayor, this.ladoMenor);
		return super.imprimir() + salida;
	}

}
