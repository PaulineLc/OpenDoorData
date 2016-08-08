package com.example.root.everythingisawesome;

import android.content.Context;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Thread t = new Thread() {

            @Override
            public void run() {
                try {
                    while (!isInterrupted()) {
                        Thread.sleep(1000);
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                String my_text = getMacId();
                                TextView my_textview = (TextView) findViewById(R.id.textView1);

                                String currentRoom = "";

                                if (my_text.equals("4c:72:b9:1f:08:18")) {
                                    currentRoom = "Home";
                                } else if (my_text.equals("6c:99:89:99:cc:30")) {
                                    currentRoom = "B0.03";
                                } else if (my_text.equals("6c:99:89:99:d7:0f")) {
                                    currentRoom = "B0.04";
                                }else if (my_text.equals("6c:99:89:a1:e5:af")) {
                                    currentRoom = "B0.02";
                                } else {
                                    currentRoom = "unknown";
                                }

                                my_textview.setText("BSSID:" + my_text +
                                        "\n" +
                                        "Current room:\n" +
                                        currentRoom);
                            }
                        });
                    }
                } catch (InterruptedException e) {
                }
            }
        };

        t.start();
    }

    public String getMacId() {

        WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        return wifiInfo.getBSSID();
    }

}