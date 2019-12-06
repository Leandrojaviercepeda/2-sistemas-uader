package ej2;

/**
 * @author Leandro Javier Cepeda
 * 
 */
public class Elipse extends Forma {

	private double radioMayor, radioMenor;

	/**
	 * Constructor.
	 * 
	 * @param String nombre: nombre de la forma.
	 * @param String color: color de la forma.
	 * @param Punto  centro: coordenada x, coordenada y.
	 * @param Double radioMayor: radio mayor del elipse.
	 * @param Double radioMenor: radio menor del elipse.
	 */
	public Elipse(Punto centro, String color, String nombre, double radioMayor, double radioMenor) {
		super(centro, color, nombre);
		this.radioMayor = radioMayor;
		this.radioMenor = radioMenor;
	}

	public double getRadioMayor() {
		return radioMayor;
	}

	public void setRadioMayor(double radioMayor) {
		this.radioMayor = radioMayor;
	}

	public double getRadioMenor() {
		return radioMenor;
	}

	public void setRadioMenor(double radioMenor) {
		this.radioMenor = radioMenor;
	}

	/**
	 * Muestra el Elipse.
	 * 
	 * @return String datos: centro, color, nombre, radio mayor, radio menor.
	 */
	public String imprimir() {
		String salida = String.format("\nRadio mayor: %f \nRadio menor: %f", this.radioMayor, this.radioMenor);
		return super.imprimir() + salida;
	}

	/**
	 * Calcula el area del Elipse.
	 * 
	 * @return Double area
	 */
	public double area() {
		return Math.PI * this.radioMayor * this.radioMenor;
	}

	/**
	 * Calcula el perimetro del Elipse.
	 * 
	 * @return Double perimetro
	 */
	public double perimetro() {
		return 2 * Math.PI * Math.sqrt((Math.pow(this.radioMayor, 2) + Math.pow(this.radioMayor, 2)) / 2);
	}

	/**
	 * Cambia el tamaño del circulo. Así, por ejemplo, si el factor vale 2, el
	 * circulo duplicará su tamaño y si es 0,5 se reducirá a la mitad.
	 * 
	 * @params Double factor: factor de escala.
	 */
	public void cambiarTamaño(double factor) {
		this.radioMayor = this.radioMayor * factor;
		this.radioMenor = this.radioMenor * factor;
	}

	/**
	 * Calcula en diametro mayor.
	 * 
	 * @return Double diametro mayor.
	 */
	public double diametroMayor() {
		return this.radioMayor * 2;
	}

	/**
	 * Calcula en diametro menor.
	 * 
	 * @return Double diametro menor.
	 */
	public double diametroMenor() {
		return this.radioMenor * 2;
	}
}
