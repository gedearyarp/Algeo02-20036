import React from 'react';
import imgDefault from "./images/imgDefault.jpg"
import uploadBigArrow from "./images/uploadBigArrow.png"

import {
  ChakraProvider,
  Box,
  Input,
  Heading,
  Text,
  extendTheme,
  Flex,
  Button,
  Spacer,
  Center,
  HStack,
  Image,
  Menu,
  MenuButton
} from '@chakra-ui/react';
import { 
  ChevronDownIcon,
  SettingsIcon,
  ArrowRightIcon
} from '@chakra-ui/icons'
import "@fontsource/poppins/400.css"
import "@fontsource/poppins/200.css"

function App() {
  //BG #282A37 CMPNT #01CC90
  const config = {
    styles: {
      global: () => ({
        body: {
          bg: "linear-gradient(90deg, rgba(40,43,56,1) 0%, rgba(51,55,72,1) 77%)",
          color: "black",
        },
        fonts: {
          heading: "Poppins",
          body: "Poppins",
        }
      }),
    },
  }

  const theme = extendTheme(config);
  
  return (
    <ChakraProvider theme={theme}>
      <Heading color="#FFFFFF" fontSize="5xl" fontFamily="poppins" textAlign="center" mt={10} mb={3} minW="100vw"> 
        Smart <span style={{ color: "#01CC90" }}>PNG</span> and <span style={{ color: "#01CC90" }}>JPEG</span> Compressor
      </Heading>
      <Text color="#FFFFFF" fontFamily="poppins" textAlign="center" fontWeight={200} fontSize="md">
        An ultimate image optimizer to compress your images
      </Text>
      <Box mt ={20} >
        <Center>
          <Button color="#01CC90" borderStyle="dotted" borderWidth={5} borderColor="#01CC90" width="30vw" height="15vh" boxShadow="xl">
            <Flex width="100%">
              <Spacer/>
              <Box>
                <Image
                  boxSize="3.5vw"
                  objectFit="cover"
                  borderRadius="3px"
                  src={uploadBigArrow}
                  alt="Upload your image"
                />
              </Box>
              <Spacer/>
              <Box>
                <Text fontSize="5xl" color="#4be3b6">Click Here!</Text>
                <Text color="#01CC90" fontSize="xl">to select your image.</Text>
              </Box>
              <Spacer/>
            </Flex>
          </Button>
        </Center>
      </Box>

      <Box mt ={5}>
        <Center>
          <Text color="#FFFFFF" fontSize="xl" fontFamily="poppins" fontWeight={200}>
            <SettingsIcon mr={5}/>  
            Additional settings <ChevronDownIcon/>
          </Text>
        </Center>
      </Box>

      <Box mt = {5}>
        <Center>
            <Flex>
              <Text color="#01CC90" fontSize="xl" fontFamily="poppins" mr={4} fontWeight={200}>
                Compression rates  
              </Text>
              <HStack maxW="320px" >
                <Input color="#FFFFFF"/>
                <Button colorScheme="teal" variant="outline">-</Button>
                <Button colorScheme="teal" variant="outline">+</Button>
              </HStack>
            </Flex>
        </Center>
      </Box>

      <Center mt ={10}>
        <Button bg="linear-gradient(90deg, rgba(1,204,144,1) 0%, rgba(43,233,177,1) 100%)" 
                color="#282A37" 
                h="6vh" 
                w="15vw" 
                boxShadow="2xl"
                fontSize="2xl">
                  Compress PNG/JPEG <ArrowRightIcon ml={2} color="black"/></Button>
      </Center>

      <Box mt = {10}>
        <Flex>
          <Spacer />
          <Box>
            <Center>
              <Text color="#FFFFFF" fontSize="3xl" fontFamily="poppins" mr={4}>
                Before
              </Text>
            </Center>
            <Image
              shadowBox="2xl"
              boxSize="20vw"
              objectFit="cover"
              borderRadius="3px"
              src={imgDefault}
              alt="Default Image"
              mt={5}
            />
          </Box>
          <Spacer />
          <Box>
            <Center>
              <Text color="#FFFFFF" fontSize="3xl" fontFamily="poppins" mr={4}>
                After
              </Text>
            </Center>
            <Image
              shadowBox="2xl"
              boxSize="20vw"
              objectFit="cover"
              borderRadius="3px"
              src={imgDefault}
              alt="Default Image"
              mt={5}
            />
          </Box>
          <Spacer />
        </Flex>
      </Box>
    </ChakraProvider>
  );
}

export default App;
