package rsa;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.math.BigInteger;

public class DescifradoVentana extends JFrame {
    private JTextField cifradoField;
    private JTextArea salidaArea;
    private RSAAlgoritmo rsa;

    public DescifradoVentana(RSAAlgoritmo rsa) {
        this.rsa = rsa;

        setTitle("Descifrado RSA");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel panel = new JPanel(new GridLayout(3, 1));
        cifradoField = new JTextField();

        JButton descifrarBtn = new JButton("Descifrar Mensaje");

        salidaArea = new JTextArea();
        salidaArea.setEditable(false);
        JScrollPane scroll = new JScrollPane(salidaArea);

        panel.add(new JLabel("Mensaje cifrado (números separados por espacio):"));
        panel.add(cifradoField);
        panel.add(descifrarBtn);

        add(panel, BorderLayout.NORTH);
        add(scroll, BorderLayout.CENTER);

        descifrarBtn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    String[] partes = cifradoField.getText().trim().split(" ");
                    BigInteger[] cifrado = new BigInteger[partes.length];
                    for (int i = 0; i < partes.length; i++) {
                        cifrado[i] = new BigInteger(partes[i]);
                    }

                    String descifrado = rsa.descifrar(cifrado);
                    salidaArea.setText("Mensaje descifrado:\n" + descifrado);

                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(null, "Error en el formato del mensaje cifrado.");
                }
            }
        });

        setVisible(true);
    }
}
