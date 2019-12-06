package ej2;

import java.util.ArrayList;

public class Provincia {

	private String nombre;
	private Pais paisPropio;
	public ArrayList<Provincia> provinciasLimite;
	public ArrayList<Pais> paisesLimite;

	public Provincia(String nombre, Pais paisPropio) {
		this.nombre = nombre;
		this.paisPropio = paisPropio;
		this.provinciasLimite = new ArrayList<Provincia>();
		this.paisesLimite = new ArrayList <Pais>();
	}

	public Pais getPaisPropio() {
		return paisPropio;
	}

	public void setPaisPropio(Pais paisPropio) {
		this.paisPropio = paisPropio;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public ArrayList<Provincia> getProvinciasLimite() {
		return provinciasLimite;
	}
	
	public void setProvinciasLimite(ArrayList<Provincia> provinciasLimite) {
		this.provinciasLimite = provinciasLimite;
	}

	public void agregarProvinciaLimite(Provincia provincia){
		this.provinciasLimite.add(provincia);
	}
	
	public void agregarPaisLimite(Pais pais){
		this.paisesLimite.add(pais);
	}
	
	public String mostrarProvinciasLimite(){
		String stringSalida = "";
		for (Provincia provincia : this.provinciasLimite) {
			stringSalida += provincia.getNombre() + ", ";
		}
		return stringSalida;
	}
	
	public String mostrarPaisesLimite(){
		String stringSalida = "";
		for (Pais pais : this.paisesLimite) {
			stringSalida += pais.getNombre() + ", ";
		}
		return stringSalida;
	}
	 
}
