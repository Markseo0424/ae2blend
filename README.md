# ae2blend
copy object datas from after effects, object can be camera or solid plane.
the data text should be :

```
Adobe After Effects 8.0 Keyframe Data

	Units Per Second	59.92
	Source Width	2160
	Source Height	2160
	Source Pixel Aspect Ratio	1
	Comp Pixel Aspect Ratio	1

Transform	Scale
	Frame	X percent	Y percent	Z percent	
		3844.46	1428.61	1098	

Transform	Position
	Frame	X pixels	Y pixels	Z pixels	
		-26817	11575.7	151183	

Transform	Orientation
	Frame	X degrees	
		353.258	68.5708	352.791	


End of Keyframe Data
```

or :
```
Adobe After Effects 8.0 Keyframe Data

	Units Per Second	59.92
	Source Width	3840
	Source Height	2160
	Source Pixel Aspect Ratio	1
	Comp Pixel Aspect Ratio	1

Transform	Position
	Frame	X pixels	Y pixels	Z pixels	
	0	1920	1080	-3432.34	
	1	1924.3	1076.85	-3442.29	
	2	1923.87	1076.48	-3447.52	
	3	1923.52	1076.64	-3453.82	
	4	1923.78	1075.32	-3462.26	
	5	1923.53	1074.43	-3469.4	
	6	1924.2	1072.83	-3477.68	
	7	1924.86	1072.32	-3485.32	
	8	1924.14	1072.13	-3488.07	
	9	1925.77	1071.27	-3493.58	
	10	1927.01	1070.6	-3497.2
  ...

Transform	Orientation
	Frame	X degrees	
	0	-0	0	-0	
	1	359.999	359.997	360	
	2	359.946	359.912	359.995	
	3	359.899	359.825	359.993	
	4	359.849	359.735	359.979	
	5	359.803	359.641	359.973	
	6	359.766	359.544	359.962	
	7	359.717	359.448	359.955	
	8	359.665	359.348	359.943	
	9	359.615	359.245	359.93	
	10	359.566	359.149	359.913	
  ...

End of Keyframe Data
```

then change 'names' to match each objects to blender objects,
change 'isCamera' to select camera object.
about scale, there are descriptions about it in python code.

after finishing all of these, just run the file!
don't forget to match focal length!
