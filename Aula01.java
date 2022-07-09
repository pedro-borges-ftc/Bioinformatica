import java.util.Scanner;

public class Aula01 {

    public static void main(String args[]) {
        Scanner ler = new Scanner(System.in);
        int num1, num2, num3, resultado;

        System.out.println( "este programa irá somar 3 números inteiro de sua escolha");

        System.out.println( "digite um número inteiro");
        num1 = ler.nextInt();

        System.out.println( "digite um número para somar ao primeiro numero");
        num2 = ler.nextInt();

        System.out.println( "digite um terceiro número para somar aos outros 2 números");
        num3 = ler.nextInt();

        resultado = num1 + num2 + num3;

        System.out.println( "o resultado é: " + resultado);
    }
    
}
