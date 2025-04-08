/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pkg04aes;

/**
 *
 * @author Alumno
 */ 
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)throws Exception {
        // TODO code application logic here
        System.out.println("Ejemplo del cifrado AES");
        String mensaje ="Habia una vez un patito que decia miau miau";
        String mensajeCifrado= CifradorAES.encrypt(mensaje);
        System.out.println("El mensaje cifrado es: " + mensajeCifrado);
        
        String mensajeDescifrado= CifradorAES.decrypt(mensaje);
        System.out.println("El mensaje descifrado es: "+ mensajeDescifrado);
    }
    
}
