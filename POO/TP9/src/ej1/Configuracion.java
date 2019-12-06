package ej1;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Configuracion {

	private Properties propiedades;
	private InputStream entrada;
	private static Configuracion configuracion;

	private Configuracion() throws IOException {
		propiedades = new Properties();
		entrada = new FileInputStream("/home/lean/MEGAsync/git/UADER/2°Sistemas/POO/TP9/properties/configuracion.properties");
		// cargamos el archivo de propiedades
		propiedades.load(entrada);
	}

	public static Configuracion getInstance() {
		if (configuracion == null)
			try {
				configuracion = new Configuracion();
			} catch (IOException ex) {
				Logger.getLogger(Configuracion.class.getName()).log(Level.SEVERE, null, ex);
			}
		return configuracion;
	}

	public String getMensaje(String clave) {
		return propiedades.getProperty(clave);
	}
}