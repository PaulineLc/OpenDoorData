package com.example.root.everythingisawesome;

import android.content.Context;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
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
                                if (isConnectedToWifi()) {

                                    String currentBSSID = getMacId();
                                    TextView textView = (TextView) findViewById(R.id.textView1);

                                    String currentRoom = "";

                                    if (currentBSSID.equals("6c:99:89:99:cc:3f")) {
                                        currentRoom = "B0.02";
                                    } else if (currentBSSID.equals("6c:99:89:a1:e5:af")) {
                                        currentRoom = "B0.03";
                                    } else if (currentBSSID.equals("6c:99:89:99:d7:0f")) {
                                        currentRoom = "B0.04";
                                    } else {
                                        currentRoom = "unknown room";
                                    }

                                    textView.setText("BSSID:" + currentBSSID +
                                            "\n" +
                                            "Current room:" + currentRoom + "\n" +
                                            "Signal strenght: " + getSignalStrenght() +
                                            "\nTime: " + System.currentTimeMillis());
                                } else {
                                    TextView my_textview = (TextView) findViewById(R.id.textView1);
                                    my_textview.setText("Wifi disconnected");
                                }
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
        //wifiManager.reassociate();
        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        return wifiInfo.getBSSID();
    }

    public int getSignalStrenght() {
        WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        return wifiInfo.getRssi();
    }

    public void refreshWifi(View view) {
        WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
        wifiManager.reassociate();
    }

    public boolean isConnectedToWifi() {
        WifiManager wifiMgr = (WifiManager) getSystemService(Context.WIFI_SERVICE);
        if (wifiMgr.isWifiEnabled()) { // WiFi adapter is ON
            WifiInfo wifiInfo = wifiMgr.getConnectionInfo();
            if( wifiInfo.getNetworkId() == -1 ){
                return false; // Not connected to an access-Point
            }
            return true;      // Connected to an Access Point
        } else {
            return false; // WiFi adapter is OFF
        }
    }





}