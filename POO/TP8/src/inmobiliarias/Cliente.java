// Cliente.java

package inmobiliarias;

public class Cliente implements Notificable {

	String nombre;
	String telefono;
	String email;

	public Cliente(String nombre, String telefono, String email) {
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

	// los 3 m�todos que siguen ya implementaban los de Notificable:
	public void avisarCambioPrecio(Inmueble x, int nuevoPrecio) {
		String mensaje = String.format("El inmueble %s en el que estaba interesado ha cambiado de precio. Hoy cuesta $%d.", x.getDomicilio(), nuevoPrecio);
		System.out.println(MailUtil.enviarMail(this, mensaje, "con nuevo precio"));
	}

	public void avisarReserva(Inmueble x) {
		String mensaje = String.format("El inmueble ubicado en %s, en el que estaba interesado ha sido reservado.", x.getDomicilio());
		System.out.println(MailUtil.enviarMail(this, mensaje, "reservado"));
	}

	public void avisarVenta(Inmueble x) {
		String mensaje = String.format("El inmueble ubicado en %s, en el que estaba interesado ha sido vendido.", x.getDomicilio());
		System.out.println(MailUtil.enviarMail(this, mensaje, "vendido"));
	}

	public String imprimirDatos() {
		String salida = String.format("\nNombre: %s.\nTelefono: %s.\nEmail: %s.\n", this.getNombre(), this.getTelefono(),
				this.getEmail());
		return salida;
	}

}
