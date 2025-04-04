package pkg03_des;

import java.io.*;
import java.security.*;
import javax.crypto.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Main {
    private static SecretKey clave;
    private static File selectedFile;

    public static void main(String[] args) {
        System.out.println("Iniciando programa...");
        generarClaveDES();
        crearInterfaz();
    }

    private static void generarClaveDES() {
        try {
            System.out.println("Generando clave DES...");
            KeyGenerator generadorDES = KeyGenerator.getInstance("DES");
            generadorDES.init(56);
            clave = generadorDES.generateKey();
            System.out.println("Clave DES generada correctamente.");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error al generar la clave DES.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private static void crearInterfaz() {
        JFrame frame = new JFrame("Cifrado DES");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 150);
        frame.setLayout(new FlowLayout());
 
        JButton btnCargar = crearBoton("Cargar Archivo");
        JButton btnCifrar = crearBoton("Cifrar");
        JButton btnDescifrar = crearBoton("Descifrar");

        btnCargar.addActionListener(e -> cargarArchivo());
        btnCifrar.addActionListener(e -> cifrarArchivo());
        btnDescifrar.addActionListener(e -> descifrarArchivo());

        frame.add(btnCargar);
        frame.add(btnCifrar);
        frame.add(btnDescifrar);

        System.out.println("Ventana de interfaz creada.");
        frame.setVisible(true);
    }

    private static JButton crearBoton(String texto) {
        JButton boton = new JButton(texto);
        boton.setBackground(new Color(60, 179, 113)); 
        boton.setForeground(Color.WHITE); 
        boton.setFont(new Font("Roboto", Font.BOLD, 14));
        boton.setPreferredSize(new Dimension(150, 40));
        boton.setBorder(BorderFactory.createLineBorder(new Color(34, 139, 34), 2));
        boton.setFocusPainted(false);
        return boton;
    }

    private static void cargarArchivo() {
        System.out.println("Abriendo diálogo para cargar archivo...");
        JFileChooser fileChooser = new JFileChooser();
        if (fileChooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            selectedFile = fileChooser.getSelectedFile();
            JOptionPane.showMessageDialog(null, "Archivo seleccionado: " + selectedFile.getName());
            System.out.println("Archivo seleccionado: " + selectedFile.getAbsolutePath());
        }
    }

    private static void cifrarArchivo() {
        if (selectedFile == null) {
            JOptionPane.showMessageDialog(null, "Seleccione un archivo primero.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        try {
            System.out.println("Cifrando archivo: " + selectedFile.getName());
            Cipher cifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cifrador.init(Cipher.ENCRYPT_MODE, clave);
            procesarArchivo(selectedFile.getAbsolutePath(), selectedFile.getAbsolutePath() + ".cifrado", cifrador);
            JOptionPane.showMessageDialog(null, "Archivo cifrado con éxito: " + selectedFile.getName() + ".cifrado");
            System.out.println("Archivo cifrado con éxito.");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error al cifrar el archivo.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private static void descifrarArchivo() {
        if (selectedFile == null) {
            JOptionPane.showMessageDialog(null, "Seleccione un archivo primero.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        File archivoCifrado = new File(selectedFile.getAbsolutePath() + ".cifrado");
        if (!archivoCifrado.exists()) {
            JOptionPane.showMessageDialog(null, "No se encontró el archivo cifrado.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        try {
            System.out.println("Descifrando archivo: " + archivoCifrado.getName());
            Cipher cifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cifrador.init(Cipher.DECRYPT_MODE, clave);

            // Sólo procesamos el archivo y mostramos el texto descifrado
            byte[] textoDescifrado = procesarArchivoYObtenerTexto(archivoCifrado.getAbsolutePath(), cifrador);
            String texto = new String(textoDescifrado, "UTF-8");
            JOptionPane.showMessageDialog(null, "Texto descifrado:\n" + texto);
            System.out.println("Archivo descifrado con éxito.");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error al descifrar el archivo.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private static byte[] procesarArchivoYObtenerTexto(String archivoEntrada, Cipher cifrador) throws Exception {
        FileInputStream entrada = new FileInputStream(archivoEntrada);
        ByteArrayOutputStream salida = new ByteArrayOutputStream();

        byte[] buffer = new byte[1000];
        int bytesLeidos;
        while ((bytesLeidos = entrada.read(buffer)) != -1) {
            byte[] bufferProcesado = cifrador.update(buffer, 0, bytesLeidos);
            salida.write(bufferProcesado);
        }

        byte[] bufferFinal = cifrador.doFinal();
        salida.write(bufferFinal);

        entrada.close();
        salida.close();

        return salida.toByteArray();
    }

    private static void procesarArchivo(String archivoEntrada, String archivoSalida, Cipher cifrador) throws Exception {
        FileInputStream entrada = new FileInputStream(archivoEntrada);
        FileOutputStream salida = new FileOutputStream(archivoSalida);

        byte[] buffer = new byte[1000];
        int bytesLeidos;
        while ((bytesLeidos = entrada.read(buffer)) != -1) {
            byte[] bufferProcesado = cifrador.update(buffer, 0, bytesLeidos);
            salida.write(bufferProcesado);
        }

        byte[] bufferFinal = cifrador.doFinal();
        salida.write(bufferFinal);

        entrada.close();
        salida.close();
    }
}
