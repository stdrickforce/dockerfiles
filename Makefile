py-ticktock: ./docker/ticktock.df
	docker build -t stdrickforce/ticktock -f docker/ticktock.df .
	docker push stdrickforce/ticktock
