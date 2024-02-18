MFR-Gateway
===========

Installation
------------

.. attention:: Die Installation des MFR-Gateways darf nur im spannungslosen Zustand des MFR-Reglers erfolgen.

WLAN Konfiguration
------------------

Wenn das MFR-Gateway startet, wird er im Stationsmodus eingerichtet und versucht, eine Verbindung zu einem zuvor gespeicherten Access Point herzustellen (eine bekannte Kombination aus SSID und Passwort).

Wenn dieser Prozess fehlschlägt, wird das MFR-Gateway in den Access Point-Modus versetzt.

Stellen Sie mit einem beliebigen Wi-Fi-fähigen Gerät mit einem Browser eine Verbindung zum neu erstellten Access Point her.

.. note:: Auf dem MFR-Gateway befindet sich ein Aufkleber mit einer einteutigen SSID (Bsp. mfr-84f3ebe02c98).
          Das Passwort für die Anmeldung am MFR-Gateway befindet sich ebenfalls am Aufkleber.

Öffnen Sie auf Ihren Smartphone die WLAN Einstellungen wählen sie den MFR-Gateway Access Point (Bsp. mfr-84f3ebe02c98) aus.
          
.. image:: /images/mfresp32_wlan_android_0_wifi_connect.png
   :scale: 100 %
   :align: center

Zur Herstellung der Verbindung erscheind ein Anmeldebildschirm.

.. image:: /images/mfresp32_wlan_android_1_wifi_password.png
   :scale: 100 %
   :align: center

Hier müssen sie das Passwort des MFR-Gateways eingeben und mit der Taste "VERBINDEN" bestätigen.

.. note:: Das Passwort befindet sich am Aufkleber des MFR-Gateways.

Nach der erfolgreichen Anmeldung sind Sie mit dem MFR-Gateway Access Point verbunden.

.. image:: /images/mfresp32_wlan_android_2_wifi_connected.png
   :scale: 100 %
   :align: center
   
Öffnen Sie den Web-Browser und geben Sie die IP-Adresse 10.10.0.1 ein.

Sie werden zu einer Webseite unter 10.10.0.1 weitergeleitet, auf der Sie die WLAN-Anmeldeinformationen Ihres MFR-Gateways konfigurieren können.

.. image:: /images/mfresp32_wlan_android_3_manager_configure_wifi.png
   :scale: 100 %
   :align: center

Klicken Sie auf die Schaltfläche "Configure WiFi" (WLAN konfigurieren):

.. image:: /images/mfresp32_wlan_android_4_manager_configure_ssid.png
   :scale: 100 %
   :align: center

Wählen Sie Ihr gewünschtes Netzwerk aus, indem Sie auf den Namen tippen (in meinem Fall "SSID"). Die SSID sollte sofort übernommen werden.

Geben Sie anschließend Ihr Passwort ein und drücken Sie die Taste „Verbinden“.

.. image:: /images/mfresp32_wlan_android_5_manager_configure_password.png
   :scale: 100 %
   :align: center

Nach erfolgreicher Verbindung erscheind.

.. image:: /images/mfresp32_wlan_android_6_manager_connected.png
   :scale: 100 %
   :align: center

Sobald eine neue SSID und ein neues Passwort festgelegt wurden, wird das ESP neu gestartet und versucht, eine Verbindung zu Ihren WLAN herzustellen.

Wenn eine Verbindung zu Ihren WLAN hergestellt wird, wird der Vorgang erfolgreich abgeschlossen. Andernfalls wird das MFR-Gateway wieder als Access Point eingerichtet.
