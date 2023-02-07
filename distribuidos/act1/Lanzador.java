package act1;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class Lanzador {
	public static void main(String[] args) {
		int BUFFER = 100_000_000;
		try {
			String path = "numeros.txt";
			BufferedReader br = new BufferedReader(new FileReader(path));
			String line = "";
			int[] numeros = new int[BUFFER];
			int index = 0;
			
			while((line = br.readLine()) != null) {
				String[] values = line.split(",");
				for (int i = 0; i < values.length; i++) {
					numeros[index++] = Integer.parseInt(values[i]);
				}
			}
			int pasos = Math.round(index / 4);
			Promediador prom1 = new Promediador(0, Arrays.copyOfRange(numeros, 0, pasos));
			prom1.start();
			Promediador prom2 = new Promediador(1, Arrays.copyOfRange(numeros, pasos + 1, pasos * 2));
			prom2.start();
			Promediador prom3 = new Promediador(2, Arrays.copyOfRange(numeros, pasos * 2 + 1, pasos * 3));
			prom3.start();
			Promediador prom4 = new Promediador(3, Arrays.copyOfRange(numeros, pasos * 3 + 1, pasos * 4));
			prom4.start();
			
			prom1.join();
			prom2.join();
			prom3.join();
			prom4.join();

			double finalRes = (prom1.res + prom2.res + prom3.res + prom4.res) / 4;
			
			System.out.println("La cantidad de números es: " + index);
			System.out.println("El promedio total es: " + finalRes);
			
			br.close();
		} catch (FileNotFoundException e) {
			System.out.println("El archivo no se encuentra, intentelo nuevamente");
		} catch (IOException e) {
			System.out.println("Ocurrio un problema al leer el archivo: " + e);
		} catch (InterruptedException e) {
			System.out.println("El hilo fue interrumpido: " + e);
		}
	
	}
}
