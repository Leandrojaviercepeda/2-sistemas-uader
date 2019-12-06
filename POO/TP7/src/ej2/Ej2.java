package ej2;

public class Ej2 {

	public static void main(String[] args) {

		// Comprobando funcionamiento de las funciones miembro de la clase Punto.
		System.out.println("Instancia de la clase Punto.");
		Punto punto = new Punto(1, 1);
		System.out.println("\nPunto: " + punto.imprimir());

		// Comprobando funcionamiento de las funciones miembro de la clase Forma.
		System.out.println("\nInstancia de la clase Forma.");
		Forma forma = new Forma(punto, "Negro", "Forma");
		System.out.println(forma.imprimir());
		forma.mover(10, 10);
		System.out.println("\nMovemos la Forma." + forma.imprimir());

		// Casteo de Forma como Rectangulo.
		System.out.println("\nCasteo de Forma como Rectangulo");
		Forma castRectangulo = new Rectangulo(new Punto(1, 1), "Blanco", "Rectangulo", 4.00, 2.00);
		System.out.println(castRectangulo.imprimir());
		castRectangulo.mover(15, 15);
		System.out.println("\nMovemos el Rectangulo." + castRectangulo.imprimir());
		System.out.println("\nArea del Rectangulo: " + ((Rectangulo) castRectangulo).area());
		System.out.println("\nPerimetro del Rectangulo: " + ((Rectangulo) castRectangulo).perimetro());
		((Rectangulo) castRectangulo).cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + castRectangulo.imprimir());

		// Casteo de Forma como Cuadrado.
		System.out.println("\nCasteo de Forma como Cuadrado");
		Forma castCuadrado = new Cuadrado(new Punto(1, 1), "Blanco", "Cuadrado", 4.00);
		System.out.println(castCuadrado.imprimir());
		castCuadrado.mover(15, 15);
		System.out.println("\nMovemos el Cuadrado." + castCuadrado.imprimir());
		System.out.println("\nArea del Cuadrado: " + ((Cuadrado) castCuadrado).area());
		System.out.println("\nPerimetro del Cuadrado: " + ((Cuadrado) castCuadrado).perimetro());
		((Cuadrado) castCuadrado).cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + castCuadrado.imprimir());

		// Casteo de Forma como Elipse.
		System.out.println("\nCasteo de Forma como Elipse");
		Forma castElipse = new Elipse(new Punto(1, 1), "Blanco", "Elipse", 4.00, 2.00);
		System.out.println(castElipse.imprimir());
		castElipse.mover(15, 15);
		System.out.println("\nMovemos el Elipse." + castElipse.imprimir());
		System.out.println("\nArea del Elipse: " + ((Elipse) castElipse).area());
		System.out.println("\nPerimetro del Elipse: " + ((Elipse) castElipse).perimetro());
		((Elipse) castElipse).cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + castElipse.imprimir());

		// Casteo de Forma como Circulo.
		System.out.println("\nCasteo de Forma como Circulo");
		Forma castCirculo = new Circulo(new Punto(1, 1), "Blanco", "Circulo", 4.00);
		System.out.println(castCirculo.imprimir());
		castCirculo.mover(15, 15);
		System.out.println("\nMovemos el Circulo." + castCirculo.imprimir());
		System.out.println("\nArea del Circulo: " + ((Circulo) castCirculo).area());
		System.out.println("\nPerimetro del Circulo: " + ((Circulo) castCirculo).perimetro());
		((Circulo) castCirculo).cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + castCirculo.imprimir());

		// Comprobando funcionamiento de las funciones miembro de la clase Rectangulo.
		System.out.println("\nInstancia de la clase Rectangulo");
		Rectangulo rectangulo = new Rectangulo(new Punto(1, 1), "Blanco", "Rectangulo", 4.00, 2.00);
		System.out.println(rectangulo.imprimir());
		rectangulo.mover(15, 15);
		System.out.println("\nMovemos el Rectangulo." + rectangulo.imprimir());
		System.out.println("\nArea del Rectangulo: " + rectangulo.area());
		System.out.println("\nPerimetro del Rectangulo: " + rectangulo.perimetro());
		rectangulo.cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + rectangulo.imprimir());

		// Comprobando funcionamiento de las funciones miembro de la clase Cuadrado.
		System.out.println("\nInstancia de la clase Cuadrado");
		Cuadrado cuadrado = new Cuadrado(new Punto(1, 1), "Blanco", "Cuadrado", 4.00);
		System.out.println(cuadrado.imprimir());
		cuadrado.mover(15, 15);
		System.out.println("\nMovemos el Cuadrado." + cuadrado.imprimir());
		System.out.println("\nArea del Cuadrado: " + cuadrado.area());
		System.out.println("\nPerimetro del Cuadrado: " + cuadrado.perimetro());
		cuadrado.cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + cuadrado.imprimir());

		// Casteo de Rectangulo como Cuadrado.
		System.out.println("\nCasteo de la clase Forma como Cuadrado");
		Rectangulo cast2Cuadrado = new Cuadrado(new Punto(1, 1), "Blanco", "Cuadrado", 4.00);
		System.out.println(cast2Cuadrado.imprimir());
		cast2Cuadrado.mover(15, 15);
		System.out.println("\nMovemos el Cuadrado." + cast2Cuadrado.imprimir());
		System.out.println("\nArea del Cuadrado: " + ((Cuadrado) cast2Cuadrado).area());
		System.out.println("\nPerimetro del Cuadrado: " + ((Cuadrado) cast2Cuadrado).perimetro());
		((Cuadrado) cast2Cuadrado).cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + cast2Cuadrado.imprimir());

		// Comprobando funcionamiento de las funciones miembro de la clase Elipse.
		System.out.println("\nInstancia de la clase Elipse");
		Elipse elipse = new Elipse(new Punto(1, 1), "Blanco", "Elipse", 4.00, 2.00);
		System.out.println(elipse.imprimir());
		elipse.mover(15, 15);
		System.out.println("\nMovemos el Elipse." + elipse.imprimir());
		System.out.println("\nArea del Elipse: " + elipse.area());
		System.out.println("\nPerimetro del Elipse: " + elipse.perimetro());
		elipse.cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + elipse.imprimir());

		// Comprobando funcionamiento de las funciones miembro de la clase Circulo.
		System.out.println("\nInstancia de la clase Circulo");
		Circulo circulo = new Circulo(new Punto(1, 1), "Blanco", "Circulo", 4.00);
		System.out.println(circulo.imprimir());
		circulo.mover(15, 15);
		System.out.println("\nMovemos el Circulo." + circulo.imprimir());
		System.out.println("\nArea del Circulo: " + circulo.area());
		System.out.println("\nPerimetro del Circulo: " + circulo.perimetro());
		circulo.cambiarTamaño(0.5);
		System.out.println("\nCambio del Tamaño: " + circulo.imprimir());

		// Casteo de Elipse como Circulo.
		System.out.println("\nCasteo de Elipse como Circulo");
		Elipse cast2Circulo = new Circulo(new Punto(1, 1), "Blanco", "Circulo", 4.00);
		System.out.println(cast2Circulo.imprimir());
		cast2Circulo.mover(15, 15);
		System.out.println("\nMovemos el Circulo." + cast2Circulo.imprimir());
		System.out.println("\nArea del Circulo: " + cast2Circulo.area());
		System.out.println("\nPerimetro del Circulo: " + cast2Circulo.perimetro());
		cast2Circulo.cambiarTamaño(4.0);
		System.out.println("\nCambio del Tamaño: " + cast2Circulo.imprimir());

		// Definiendo varias formas en una List.
		Coleccion formas = new Coleccion();
		formas.definirFormas(0, 0, "Blanco", 1);
		System.out.println("\nDefiniendo varias formas. \nFormas: ");
		System.out.println(formas.imprimir());

		// Cambiando el color de las formas y moviendolas de su posicion.
		System.out.println("\nCambiando el color de las formas y moviendolas de su posicion. \nFormas:");
		formas.redefinirPosicionYColor(5, 5, "Rojo");
		System.out.println(formas.imprimir());

		// Calculando el area y perimetro de cada forma.
		System.out.println("\nArea de las formas: \n" + formas.area());
		System.out.println("\nPerimetro de las formas: \n" + formas.perimetro());

	}

}
