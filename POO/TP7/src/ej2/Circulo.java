/**
 * 
 */
package ej2;

/**
 * @author Leandro Javier Cepeda
 *
 */
public class Circulo extends Elipse {

	private double radio;

	/**
	 * Constructor
	 * 
	 * @param Punto  centro: coordenada x, coordenada y.
	 * @param String color: color del circulo.
	 * @param String nombre: nombre del circulo.
	 * @param Double radio: radio del circulo.
	 */
	public Circulo(Punto centro, String color, String nombre, double radio) {
		super(centro, color, nombre, radio, radio);
		this.radio = radio;
	}

	public void setRadio(double radio) {
		this.radio = radio;
	}

	public double getRadio() {
		return this.radio;
	}

	public void setRadioMayor(double radio) {
		this.radio = radio;
	}

	public double getRadioMayor() {
		return this.getRadio();
	}

	public void setRadioMenor(double radio) {
		this.radio = radio;
	}

	public double getRadioMenor() {
		return this.getRadio();
	}

	public double diametroMayor() {
		return this.diametro();
	}

	public double diametroMenor() {
		return this.diametro();
	}

	/**
	 * Calcula el diametro del circulo.
	 * 
	 * @return Double diametro.
	 */
	public double diametro() {
		return (this.radio * 2);
	}

	/**
	 * Calcula el area del circulo.
	 * 
	 * @return Double area.
	 */
	public double area() {
		return (Math.PI * Math.pow(this.radio, 2));
	}

	/**
	 * Calcula el perimetro del circulo.
	 * 
	 * @return Double perimetro.
	 */
	public double perimetro() {
		return 2 * Math.PI * this.radio;
	}

	/**
	 * Cambia el tamaño del circulo. Así, por ejemplo, si el factor vale 2, el
	 * circulo duplicará su tamaño y si es 0,5 se reducirá a la mitad.
	 * 
	 * @params Double factor: factor de escala.
	 */
	public void cambiarTamaño(double factor) {
		this.radio = this.radio * factor;
	}

	/**
	 * Muestra el circulo.
	 * 
	 * @return String datos: nombre, color, centro, radio.
	 */
	public String imprimir() {
		String salida = String.format("\nForma: %s \nColor: %s \nCentro: x: %f y: %f \nRadio: %f", this.getNombre(),
				this.getColor(), this.getCentro().getX(), this.getCentro().getX(), this.radio);
		return salida;
	}

}
