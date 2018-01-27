# main execution file 

import numpy as np 
import argparse
import pickle 
from data_loader import RetailDataset, get_loader
from solver import Solver 


def main(config):
	data_loader = get_loader(path = config.data_path, 
							 batch_size = config.batch_size, 
							 num_workers = config.num_workers)
	model_dims = [(config.input_dim, 500), (500, 200), (200, 50), (50, 10), (10, 5),(5, 1)]
	solver = Solver(config, model_dims, data_loader)
	solver.train()

	test_data = np.asarray([1,2,3,4,5,6,7,8])
	solver.inference(test_data)




if __name__ == "__main__":
	parser = argparse.ArgumentParser() 

	# hyperparameters
	parser.add_argument("--data_path", type=str, default="../data/datasets.pkl")
	parser.add_argument("--model_dir", type=str, default="./models")
	parser.add_argument("--batch_size", type=int, default=64)
	parser.add_argument("--num_epochs", type=int, default=20)
	parser.add_argument("--num_workers", type=int, default=2)
	parser.add_argument("--learning_rate", type=float, default=0.0001)
	parser.add_argument("--log_step", type=int, default=100)
	parser.add_argument("--input_dim", type=int, default=8)


	config = parser.parse_args()
	print(config)
	main(config)
