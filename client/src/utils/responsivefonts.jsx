import { Dimensions, PixelRatio } from 'react-native';

const { width: SCREEN_WIDTH } = Dimensions.get('window');


const BASE_WIDTH = 430;
const scale = SCREEN_WIDTH / BASE_WIDTH;

const scaleFontSize = (size) => {
  const newSize = size * scale;
  return Math.round(PixelRatio.roundToNearestPixel(newSize));
}

export default scaleFontSize