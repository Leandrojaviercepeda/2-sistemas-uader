package inmobiliarias;

public class Escribano implements Notificable {

	private String nombre;
	private String telefono;
	private String email;

	public Escribano(String nombre, String telefono, String email) {
		this.nombre = nombre;
		this.telefono = telefono;
		this.email = email;
	}

	public String getNombre() {
		return nombre;
	}

	public String getTelefono() {
		return telefono;
	}

	public String getEmail() {
		return email;
	}

	public void setTelefono(String nuevo) {
		telefono = nuevo;
	}

	public void setEmail(String nuevo) {
		email = nuevo;
	}

	public void avisarVenta(Inmueble x) {
		String mensaje = String.format("Señor %s, debido a la realizacion de la venta de un inmueble es necesario su asistencia profesional. Comuniquese con nosotros cuando sea posible. Muchas gracias por su colaboracion.", this.getNombre());
		System.out.println(MailUtil.enviarMail(this, mensaje, "aviso"));
	}

	public void avisarCambioPrecio(Inmueble x, int nuevoPrecio) {
	}

	public void avisarReserva(Inmueble x) {
	}

	public String imprimirDatos() {
		String salida = String.format("\nNombre: %s.\nTelefono: %s.\nEmail: %s.\n", this.getNombre(), this.getTelefono(),
				this.getEmail());
		return salida;
	}

}
