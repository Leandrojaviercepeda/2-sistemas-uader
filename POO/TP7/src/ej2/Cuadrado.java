/**
 * 
 */
package ej2;

/**
 * @author Leandro Javier Cepeda
 *
 */
public class Cuadrado extends Rectangulo {

	private double lado;

	/**
	 * Constructor.
	 * 
	 * @param Punto  centro: coordenada x, coordenada y.
	 * @param String color: color del cuadrado.
	 * @param String nombre: nombre del cuadrado.
	 * @param Double lado: lado del cuadrado.
	 */
	public Cuadrado(Punto centro, String color, String nombre, double lado) {
		super(centro, color, nombre, lado, lado);
		this.lado = lado;
	}

	public double getLado() {
		return this.lado;
	}

	public void setLado(double lado) {
		this.lado = lado;
	}

	public double getLadoMayor() {
		return this.getLado();
	}
	
	public void setLadoMayor(double lado) {
		this.lado = lado;
	}
	
	public double getLadoMenor() {
		return this.getLado();
	}
	
	public void setLadoMenor(double lado) {
		this.lado = lado;
	}
	
	/**
	 * Muestra el cuadrado.
	 * 
	 * @return String salida: centro, color, nombre, lado.
	 */
	public String imprimir() {
		String salida = String.format("\nForma: %s \nColor: %s \nCentro: x: %f y: %f \nLado: %f", this.getNombre(),
				this.getColor(), this.getCentro().getX(), this.getCentro().getX(), this.lado);
		return salida;
	}

	/**
	 * Calcula el area del cuadrado.
	 * 
	 * @return Double area.
	 */
	public double area() {
		return Math.pow(this.lado, 2);
	}

	/**
	 * Calcula el perimetro del cuadrado.
	 * 
	 * @return Double perimetro.
	 */
	public double perimetro() {
		return this.lado * 4;
	}

	/**
	 * Cambia el tamaño del cuadrado. Así, por ejemplo, si el factor vale 2, el
	 * cuadrado duplicará su tamaño y si es 0,5 se reducirá a la mitad.
	 * 
	 * @params Double factor: factor de escala.
	 */
	public void cambiarTamaño(double factor) {
		this.lado = this.lado * factor;
	}
}
