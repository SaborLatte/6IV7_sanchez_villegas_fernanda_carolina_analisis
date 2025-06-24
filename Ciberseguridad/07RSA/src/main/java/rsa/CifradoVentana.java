package rsa;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.math.BigInteger;

public class CifradoVentana extends JFrame {
    private JTextField mensajeField;
    private JTextArea salidaArea;
    private RSAAlgoritmo rsa;

    public CifradoVentana() {
        setTitle("Cifrado RSA");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        rsa = new RSAAlgoritmo(4); // Primos de 3 dígitos
        rsa.generarPrimos();
        rsa.generarClaves();

        JPanel topPanel = new JPanel();
        topPanel.setLayout(new GridLayout(2, 1));

        mensajeField = new JTextField(20);
        JButton cifrarBtn = new JButton("Cifrar Mensaje");

        topPanel.add(new JLabel("Mensaje a cifrar:"));
        topPanel.add(mensajeField);
        topPanel.add(cifrarBtn);

        salidaArea = new JTextArea();
        salidaArea.setEditable(false);
        JScrollPane scroll = new JScrollPane(salidaArea);

        JButton irDescifrado = new JButton("Ir a Descifrado");

        add(topPanel, BorderLayout.NORTH);
        add(scroll, BorderLayout.CENTER);
        add(irDescifrado, BorderLayout.SOUTH);

        cifrarBtn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String mensaje = mensajeField.getText();
                BigInteger[] cifrado = rsa.cifrar(mensaje);

                StringBuilder sb = new StringBuilder();
                sb.append("=== Claves RSA ===\n");
                sb.append("p: ").append(rsa.p).append("\n");
                sb.append("q: ").append(rsa.q).append("\n");
                sb.append("n: ").append(rsa.n).append("\n");
                sb.append("φ(n): ").append(rsa.fi).append("\n");
                sb.append("e: ").append(rsa.e).append("\n");
                sb.append("d: ").append(rsa.d).append("\n\n");

                sb.append("Mensaje cifrado:\n");
                for (BigInteger bi : cifrado) {
                    sb.append(bi.toString()).append(" ");
                }

                salidaArea.setText(sb.toString());
            }
        });

        irDescifrado.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                new DescifradoVentana(rsa);
            }
        });

        setVisible(true);
    }
}
