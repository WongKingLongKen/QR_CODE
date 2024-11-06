import segno

qrcode = segno.make_qr("Harsh is handsome")
qrcode.save("qrcode.png",
            scale=10,
            border=20,
            light=(00, 101, 100),
            dark=(198, 194, 193),
            quiet_zone=(220, 211, 188),
            data_dark=(235, 237, 236),
            data_light=(198, 194, 193),
            )

