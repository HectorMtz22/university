package red;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

public class Estructura {
    int nK[] = {2, 3, 3, 1};
    double[][][] w = new double[nK.length][9][9];
    double[][] s = new double[nK.length][9];

    final int x1[] = {34};
    final int x2[] = {23};
    final int d1[] = {57};

    public void estruct() {
        int row = 1;
        for (int i = 0; i < nK.length; i++) {
            row *= nK[i];
        }

        double[] vw = new double[row];
        for (int i = 0; i < vw.length; i++) {
            vw[i] = new Random().nextDouble();
        }
    }
    private void propagacion_hacia_delante(double[] vw) {
        List<Double> lw = new ArrayList<>();
        for (int i = 0; i < vw.length; i++) {
            lw.add(vw[i]);
        }
        Iterator wi = lw.iterator();
        System.out.println("* Entradas (x1, x2): ");
        int k = 0;
        s[k][0] = x1[0] / 100.0;
        s[k][1] = x2[0] / 100.0;
        System.out.println("s[" + k + "][" + 0 + "] = " + s[k][0]);
        System.out.println("s[" + k + "][" + 1 + "] = " + s[k][1]);
        double aux;
        for (k = 1; k < nK.length; k++) { 
            System.out.println("\n*Capa(k): " + k);
            for (int j = 0; j < nK[k]; j++) {
                aux = 0.0;
                for (int i = 0; i < nK[k - 1]; i++) {
                    if (wi.hasNext()) {
                        w[k][j][i] = (double) wi.next();
                        System.out.println("w[" + k + "][" + j + "][" + i + "] = " + w[k][j][i]);
                        aux += s[k - 1][i] * w[k][j][i];
                    }
                }

                System.out.println("s[" + k + "][" + j + "] = ");
            }
        }
        double error = error(s[nK.length - 1][0]); System.out.println("Error(%) = " + error + "\n");
    }
    private double error(double salida) { System.out.println("\nCalculando error: ");
        System.out.println("Salida real (s) = " + salida); 
        System.out.println("Salida deseada (d1) = " + d1[0] /
        100.0);
        double error = (d1[0] / 100.0) - salida;
        return Math.abs(error) * 100.0;
    }
    // función de activación(F)
    public double F(double n) {
        return 1 / (1 + Math.pow(Math.E, -n));
    }
}
