package inmobiliarias;

public class MailUtil {

	public MailUtil() {

	}

	public static String enviarMail(Notificable notificable, String mensaje, String evento) {
		String destinatario = String.format("Destinatario: %s.\nEmail: %s", notificable.getNombre(), notificable.getEmail());
		String asunto = String.format("\nAsunto: %s.", evento);
		String cuerpo = String.format("\n%s\n", mensaje);
		return destinatario + asunto + cuerpo;
	}
}
