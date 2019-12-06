package ej2;

import java.util.ArrayList;

public class Continente {

	private String nombre;
	public ArrayList<Pais> paises;

	public Continente(String nombre) {
		this.nombre = nombre;
		this.paises = new ArrayList<Pais>();
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public ArrayList<Pais> getPaises() {
		return paises;
	}

	public void setPaises(ArrayList<Pais> paises) {
		this.paises = paises;
	}

	public void agregarPais(Pais pais){
		this.paises.add(pais);
	}
	
	public String mostrarPaises(){
		String stringSalida = "";
		for (Pais pais : this.paises) {
			stringSalida += pais.getNombre() + ", ";
		}
		return stringSalida;
	}

	
}
