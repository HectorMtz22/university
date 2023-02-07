package act1;

public class Promediador extends Thread {
	int id;
	int[] data;
	double res = 0.0;
	public Promediador(int id, int[] data) {
		this.id = id;
		this.data = data;
	}
	double suma = 0;
	public void run() {
		for (int i = 0; i < data.length; i++) {
			suma += data[i];
		}
		res = suma / data.length;
		System.out.println("Hilo " + id + " suma: " + suma + " y promedio " + res);
	}
}
