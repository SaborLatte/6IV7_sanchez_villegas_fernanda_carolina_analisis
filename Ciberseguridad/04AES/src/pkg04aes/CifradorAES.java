/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pkg04aes;

/**
 *
 * @author Alumno
 */
import java.security.*;
import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
import sun.misc.*;

public class CifradorAES {
    //generar las subllaves y los métodos para cifrar y descifrar 
    
    //crear un método para la llave
    
    public static final byte[] keyvalue = new byte[]{
    /*
        Recordemos que dentro de AES se va a manejar diferentes 
        tamaños de la llave de acuerdo al tipo de operación
        128 16 caracteres 9 rondas
        192 24 caracteres 11 rondas
        256 32 caracteres 13 rondas
        */
        'q', 'w','e','r','t','y','u','i',
        'q', 'w','e','r','t','y','u','i'
    };
    private static final String instancia= "AES";
    
    public static String encrypt(String Data)throws Exception{
    /*Para poder cifrar debemos generar las subcalves necesarias 
        para ejecutar el algoritmo acorde al numero de rondas, par ello va,os a usar 
        un método de generación de claves
        */
    Key subllave= generateKey();
    
    //inicializamos el cifrado
        Cipher cifrado =Cipher.getInstance(instancia);
        cifrado.init(Cipher.ENCRYPT_MODE, subllave);
    //vamos a obtener el mensaje que se quiere cifrar y lo transformamos en bytes
    byte[] encValores= cifrado.doFinal(Data.getBytes());
        System.out.println("Mensaje Cifrado: " 
                + encValores);
        
    //formato de codificacipon base 64 a partir de la libreria sun con un objeto base 64 BASE640Encoder
    
    //String valoresencriptadosformat= new BASE64Encoder().encode(encValores);
    
    String cadenaEncriptada= encValores.toString();
    return cadenaEncriptada;
    }
    public static String decrypt(String valoresEncriptados)throws Exception{
    /*Para poder cifrar debemos generar las subcalves necesarias 
        para ejecutar el algoritmo acorde al numero de rondas, par ello va,os a usar 
        un método de generación de claves
        */
    Key subllave= generateKey();
    
    //inicializamos el cifrado
        Cipher cifrado =Cipher.getInstance(instancia);
        cifrado.init(Cipher.DECRYPT_MODE, subllave);
    //vamos a obtener el mensaje que se quiere cifrar y lo transformamos en bytes
   // byte[] decoValores= new BASE64Decoder().decodeBuffer(valoresEncriptados);
   byte [] decValores= cifrado.doFinal(valoresEncriptados.getBytes());
        System.out.println("Mensaje Cifrado: " 
                + decValores);
        
    //formato de codificacipon base 64 a partir de la libreria sun con un objeto base 64 BASE640Encoder
    
    //String valoresencriptadosformat= new BASE64Encoder().encode(encValores);
    
    String valoresDescifrados= new String(decValores);
    return valoresDescifrados;
    }
    private static Key generateKey()throws Exception{
    //vamos a ocupar llaves a partir de SecretKeySpec
    
    Key subllavekawaii=new SecretKeySpec(keyvalue, instancia);
            return subllavekawaii;
    }
}
